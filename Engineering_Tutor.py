```python
import streamlit as st

st.set_page_config(
    page_title="Jakobura Engineering Physics Tutor",
    page_icon="⚙️"
)

st.title("⚙️ Jakobura Engineering Physics Tutor")
st.write("Ask questions about PHY 122 Engineering Physics.")

# Response function
def tutor_response(question):
    q = question.lower()

    if "mechanics" in q:
        return """
### Mechanics

Mechanics is the branch of physics that studies the motion of objects and the forces acting on them.

Major topics include:

- Kinematics
- Dynamics
- Work and Energy
- Momentum
- Rotational Motion
- Equilibrium and Statics

Mechanics forms the foundation of Engineering Physics.
"""

    elif "kinematics" in q:
        return """
### Kinematics

Kinematics describes motion without considering the forces causing the motion.

Important equations:

v = u + at

s = ut + ½at²

v² = u² + 2as

where:

- u = initial velocity
- v = final velocity
- a = acceleration
- t = time
- s = displacement
"""

    elif "newton" in q:
        return """
### Newton's Laws

1. First Law:
   An object remains at rest or in uniform motion unless acted upon by a net force.

2. Second Law:
   F = ma

3. Third Law:
   For every action there is an equal and opposite reaction.
"""

    elif "force" in q:
        return """
### Force

Force is a push or pull acting on an object.

SI Unit: Newton (N)

Equation:

F = ma

where:

- F = force
- m = mass
- a = acceleration
"""

    elif "energy" in q:
        return """
### Energy

Energy is the ability to do work.

Kinetic Energy:

KE = ½mv²

Potential Energy:

PE = mgh

Mechanical Energy:

E = KE + PE
"""

    elif "momentum" in q:
        return """
### Momentum

Momentum is the product of mass and velocity.

p = mv

where:

- p = momentum
- m = mass
- v = velocity

The SI unit is kg·m/s.
"""

    else:
        return """
I am a PHY 122 Engineering Physics Tutor.

Try asking about:

- Mechanics
- Kinematics
- Newton's Laws
- Force
- Work
- Energy
- Momentum
- Circular Motion
- Torque
- Equilibrium
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a PHY 122 question...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = tutor_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)
```
