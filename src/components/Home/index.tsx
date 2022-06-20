import { setStatusBarBackgroundColor, StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { View, Text, Button } from 'react-native';
import {styles} from './styles';
export function Home() {

    const [mensagem, setMensagem] = useState("Campo de informação");

    return (

        <View style={styles.container}>

            <Text
                key={"compo_info"}
                style={styles.info}
                accessibilityLabel="campo_info"
                >
                    
                {mensagem}
            </Text>

            <View style={styles.viewBotao}>
                <Button
                    key={"botao1"}
                    accessibilityLabel="botao1"
                    title='Botão 1'
                    onPress={() => {
                        setMensagem("texto 1")
                    }}
                />
                <Button
                    key={"botao2"}
                    accessibilityLabel="botao2"
                    title='Botão 2'
                    onPress={() => {
                        setMensagem("texto 2")
                    }} 
                />
                <Button
                    key={"botao3"}
                    accessibilityLabel="botao3"
                    title='Botão 3' 
                    onPress={() => {
                        setMensagem("texto 2")
                    }}
                />

            </View>
            
        </View>
    );
}