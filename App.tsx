import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, TouchableOpacity, TouchableOpacityBase, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import {Home} from './src/components/Home'

const Stack = createNativeStackNavigator();

export default function App() {
 
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Hello" component={Home} />
      </Stack.Navigator>
    </NavigationContainer>
    
  );
}
