<template>
  <div class="app-body">
    <div class="register-box">
      <h2>Вход</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="login" type="text" placeholder="Логин" required />
        <input v-model="password" type="password" placeholder="Пароль" required />
        <div class="button-container">
          <button @click="handleLogin" type="submit" class="login-btn">Войти</button>
          <button @click="handleRegister" type="button" class="register-btn">Зарегистрироваться</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const login = ref('')
const password = ref('')

const handleLogin = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: login.value,
        password: password.value,
      }),
    })

    const data = await response.json()

    if (data.success) {
      alert('✅ Успешный вход!')
      // window.location.href = '/profile'
    } else {
      alert(`❌ Ошибка входа: ${data.message}`)
    }
  } catch (error) {
    console.error('Ошибка входа:', error)
    alert('💥 Не удалось выполнить вход')
  }
}

const handleRegister = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: login.value,
        password: password.value,
      }),
    })

    const data = await response.json()

    if (data.success) {
      alert('✅ Успешная регистрация!')
      // Можно автоматически логинить или перекидывать на вход
    } else {
      alert(`❌ Ошибка регистрации: ${data.message}`)
    }
  } catch (error) {
    console.error('Ошибка регистрации:', error)
    alert('💥 Не удалось выполнить регистрацию')
  }
}
</script>



<style scoped>
.app-body {
  background-image: url('/src/assets/5053309.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: Arial, sans-serif;
}

.register-box {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px) saturate(180%);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.register-box h2 {
  color: rgb(255, 255, 255);
}

.register-box input {
  width: 100%;
  padding: 10px 15px;
  margin: 15px 0;
  border: none;
  border-radius: 5px;
  box-sizing: border-box;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}

.button-container button {
  flex: 1;
  margin: 5px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-btn {
  background: lightblue;
}

.register-btn {
  background: lightgreen;
}
</style>
