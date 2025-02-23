import streamlit as st
import math
import webbrowser

# Função para calcular volumes
def calcular_volume(forma):
    st.subheader(f"📐 Cálculo de Volume: {forma}")

    if forma == "Cubo":
        L = st.number_input("Lado (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            vcm = L ** 3
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Paralelepípedo":
        C = st.number_input("Comprimento (cm):", min_value=0.0, format="%.2f")
        L = st.number_input("Largura (cm):", min_value=0.0, format="%.2f")
        A = st.number_input("Altura (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            vcm = C * L * A
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Esfera":
        D = st.number_input("Diâmetro (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            R = D / 2
            vcm = (4 / 3) * math.pi * (R ** 3)
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Cilindro":
        D = st.number_input("Diâmetro (cm):", min_value=0.0, format="%.2f")
        A = st.number_input("Altura (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            R = D / 2
            vcm = math.pi * (R ** 2) * A
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Tronco de Cilindro":
        A1 = st.number_input("Altura do maior lado (cm):", min_value=0.0, format="%.2f")
        a2 = st.number_input("Altura do menor lado (cm):", min_value=0.0, format="%.2f")
        D1 = st.number_input("Diâmetro da base maior (cm):", min_value=0.0, format="%.2f")
        d2 = st.number_input("Diâmetro da base menor (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            H = (A1 + a2) / 2
            R1 = D1 / 2
            r2 = d2 / 2
            vcm = (math.pi * H * ((R1 ** 2) + (r2 ** 2) + (R1 * r2))) / 3
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Cone":
        D = st.number_input("Diâmetro (cm):", min_value=0.0, format="%.2f")
        A = st.number_input("Altura (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            R = D / 2
            vcm = (1 / 3) * math.pi * (R ** 2) * A
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Tronco de Cone":
        A = st.number_input("Altura (cm):", min_value=0.0, format="%.2f")
        D1 = st.number_input("Diâmetro da extremidade maior (cm):", min_value=0.0, format="%.2f")
        d2 = st.number_input("Diâmetro da extremidade menor (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            R1 = D1 / 2
            r2 = d2 / 2
            vcm = (math.pi * A * ((R1 ** 2) + (r2 ** 2) + (R1 * r2))) / 3
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

    elif forma == "Pirâmide":
        L = st.number_input("Lado da base (cm):", min_value=0.0, format="%.2f")
        A = st.number_input("Altura (cm):", min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            base = L ** 2  
            vcm = (1 / 3) * base * A
            vmm = vcm * (10 ** -6)
            vl = vmm * (10 ** 3)
            exibir_resultado(vcm, vmm, vl)

# Função para exibir os resultados
def exibir_resultado(vcm, vmm, vl):
    st.success(f"📊 **Resultados:**\n\n📏 {vcm:.2f} cm³\n📐 {vmm:.6f} m³\n🧪 {vl:.2f} L")

# Função para abrir o WhatsApp
def abrir_whatsapp():
    st.markdown("[📞 Entre em contato no WhatsApp](https://wa.me/553832142910?text=Ol%C3%A1%2C%20gostaria%20de%20fazer%20um%20or%C3%A7amento!)")

# Interface principal
st.title("🏗️ Calculadora de Volumes - Madeireira Líder")

st.sidebar.subheader("Escolha a forma geométrica")
formas = ["Cubo", "Paralelepípedo", "Esfera", "Cilindro", "Tronco de Cilindro", "Cone", "Tronco de Cone", "Pirâmide"]
escolha = st.sidebar.radio("", formas)

calcular_volume(escolha)

st.sidebar.subheader("📞 Contato")
st.sidebar.button("WhatsApp", on_click=abrir_whatsapp)
