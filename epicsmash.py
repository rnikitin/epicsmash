import math
import streamlit as st

def main():
    st.title("Epicsmash: Prioritize Anything")

    if "epics" not in st.session_state:
        st.session_state.epics = []

    if "merge_steps" not in st.session_state:
        st.session_state.merge_steps = []

    if "current_step" not in st.session_state:
        st.session_state.current_step = 0

    if "log" not in st.session_state:
        st.session_state.log = []

    if "sorted_epics" not in st.session_state:
        st.session_state.sorted_epics = []

    if "current_merge" not in st.session_state:
        st.session_state.current_merge = []

    if "left_idx" not in st.session_state:
        st.session_state.left_idx = 0

    if "right_idx" not in st.session_state:
        st.session_state.right_idx = 0

    if "left_half" not in st.session_state:
        st.session_state.left_half = []

    if "right_half" not in st.session_state:
        st.session_state.right_half = []

    if "comparison_cache" not in st.session_state:
        st.session_state.comparison_cache = {}

    if st.session_state.epics == []:
        epics_input = st.text_area("Enter your epics (one per line):", height=200)
        if st.button("Begin"):
            st.session_state.epics = [epic.strip() for epic in epics_input.split('\n') if epic.strip()]
            st.session_state.log.append(f"Input Epics: {st.session_state.epics}")
            st.session_state.merge_steps = []
            st.session_state.current_step = 0
            st.session_state.sorted_epics = []
            st.session_state.current_merge = []
            st.session_state.comparison_cache = {}
            prepare_steps(st.session_state.epics)
            st.rerun()
    else:
        merge_epics()

def prepare_steps(epics):
    if len(epics) > 1:
        mid = math.ceil(len(epics) / 2)
        left_half = epics[:mid]
        right_half = epics[mid:]
        st.session_state.log.append(f"Split: {left_half} and {right_half}")
        prepare_steps(left_half)
        prepare_steps(right_half)
        st.session_state.merge_steps.append((left_half, right_half))

def merge_epics():
    if st.session_state.current_step < len(st.session_state.merge_steps):
        left_half, right_half = st.session_state.merge_steps[st.session_state.current_step]

        if not st.session_state.current_merge:
            st.session_state.current_merge = []
            st.session_state.left_half = left_half
            st.session_state.right_half = right_half
            st.session_state.left_idx = 0
            st.session_state.right_idx = 0

        left_idx = st.session_state.left_idx
        right_idx = st.session_state.right_idx
        merged = st.session_state.current_merge

        if left_idx < len(left_half) and right_idx < len(right_half):
            left_elem = left_half[left_idx]
            right_elem = right_half[right_idx]

            if left_elem == right_elem:
                merged.append(left_elem)
                st.session_state.left_idx += 1
                st.session_state.right_idx += 1
                st.session_state.log.append(f"Step {st.session_state.current_step + 1}: Shown: ({left_elem}, {right_elem}), Automatically selected: {left_elem}")
                st.rerun()
            else:
                # Check if this comparison is in the cache
                cache_key = (left_elem, right_elem)
                if cache_key in st.session_state.comparison_cache:
                    selected_elem = st.session_state.comparison_cache[cache_key]
                    merged.append(selected_elem)
                    if selected_elem == left_elem:
                        st.session_state.left_idx += 1
                    else:
                        st.session_state.right_idx += 1
                    st.session_state.log.append(f"Step {st.session_state.current_step + 1}: Shown: ({left_elem}, {right_elem}), Cached selection: {selected_elem}")
                    st.rerun()
                else:
                    step_number = st.session_state.current_step + 1
                    st.write(f"Step {step_number}: Which epic is more important?")
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(left_elem, key=f"{left_elem}-{step_number}-left"):
                            merged.append(left_elem)
                            st.session_state.left_idx += 1
                            st.session_state.comparison_cache[cache_key] = left_elem
                            st.session_state.log.append(f"Step {step_number}: Shown: ({left_elem}, {right_elem}), Selected: {left_elem}")
                            st.rerun()
                    with col2:
                        if st.button(right_elem, key=f"{right_elem}-{step_number}-right"):
                            merged.append(right_elem)
                            st.session_state.right_idx += 1
                            st.session_state.comparison_cache[cache_key] = right_elem
                            st.session_state.log.append(f"Step {step_number}: Shown: ({left_elem}, {right_elem}), Selected: {right_elem}")
                            st.rerun()
        else:
            # Ensure all remaining elements are added
            if left_idx < len(left_half):
                merged.extend(left_half[left_idx:])
                st.session_state.log.append(f"Remaining left half elements added: {left_half[left_idx:]}")
            if right_idx < len(right_half):
                merged.extend(right_half[right_idx:])
                st.session_state.log.append(f"Remaining right half elements added: {right_half[right_idx:]}")

            st.session_state.current_merge = []
            st.session_state.left_idx = 0
            st.session_state.right_idx = 0
            st.session_state.left_half = []
            st.session_state.right_half = []

            if st.session_state.current_step + 1 < len(st.session_state.merge_steps):
                next_left_half, next_right_half = st.session_state.merge_steps[st.session_state.current_step + 1]
                st.session_state.merge_steps[st.session_state.current_step + 1] = (merged, next_right_half)
            else:
                st.session_state.sorted_epics = merged
            st.session_state.current_step += 1
            st.rerun()
    else:
        finalize_sorting()

def finalize_sorting():
    st.write("Sorting complete!")
    st.session_state.sorted_epics = list(dict.fromkeys(st.session_state.sorted_epics))  # Remove duplicates
    st.session_state.log.append(f"Output Epics: {st.session_state.sorted_epics}")
    st.text_area("Sorted Epics:", value="\n".join(st.session_state.sorted_epics), height=200)
    st.text_area("Log Output:", value="\n".join(st.session_state.log), height=200)
    if st.button("Start Again"):
        st.session_state.epics = []
        st.session_state.merge_steps = []
        st.session_state.current_step = 0
        st.session_state.sorted_epics = []
        st.session_state.current_merge = []
        st.session_state.left_idx = 0
        st.session_state.right_idx = 0
        st.session_state.left_half = []
        st.session_state.right_half = []
        st.session_state.log = []
        st.session_state.comparison_cache = {}
        st.rerun()

if __name__ == "__main__":
    main()
