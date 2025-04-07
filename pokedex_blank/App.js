import { StatusBar } from 'expo-status-bar';
import { Button, Pressable, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View> {/*Container-image*/}
        <Image source={{ uri: "" }}
          width={200}
          height={200}
        />
      </View>
      <View>{/*container-form*/}

      </View>
      <Text style={styles.title}>Iniciar Sesion</Text>{/*title*/}
      <Text style={styles.label}>Correo:</Text>
      <TextInput style={styles.input} />
      <Text style={styles.label}>Contraseña:</Text>{/*title*/}
      <TextInput style={styles.input} />
      {/* <TouchableOpacity title="enviar"/>
    <Button title="enviar"/> */}
      <Pressable style={styles.send}>
        <Text style={styles.send.textButton}>Enviar</Text>
      </Pressable>
      <View style={styles.containerFooter.alignItems}>{/* container-footer */}
        <Text>Olvidaste tu contraseña?</Text>
        <Text>Registrarse</Text>
      </View>
    </View>


  );
}

const styles = StyleSheet.create({
  container: {
    flex: 0.5,
    padding: 10,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 30,
    fontWeight: "bold"
  },
  label: {
    fontSize: 20,
    fontWeight: "bold"
  },
  input: {
    borderRadius: 10,
    borderWidth: 2,
    borderColor: "red",
    fontSize: 15,
    width: "auto",
  },
  send: {
    backgroundColor: "red",
    width: "auto",
    height: "auto",
    borderRadius: 10,
    marginTop: 15,
    alignItems: "center",
    textButton: {
      color: "black",
      fontSize: 20,
      fontWeight: "bold",
    }
  },
  containerFooter:{
    justifyContent:"center",
    alignItems:"center",
    texts:{
      fontSize:20,
      margin:5,
    }
}
});
