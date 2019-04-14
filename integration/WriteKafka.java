/*-----pom.xml------
<kafka.version>1.0.1</kafka.version>

<dependencies>
    <dependency>
        <groupId>org.apache.kafka</groupId>
        <artifactId>kafka-streams</artifactId>
        <version>${kafka.version}</version>
    </dependency>
</dependencies>

----usage------
String broker = список серверов где сохранится, будет известно когда в продаакшен все. 
                    формат будет такой "redhawk:9092,localhost:9092" и если у нас только один то "server:9092", 9092 это обычный порт для сервер kafka
    
String topic = группа или ключ. У нас по умольчайно "ru.vsuet.noses"
String key = уникальный идентификатор нос
String message = NOSE_ID, DATE, SESSION, DETAILS[default=""], s_1,...,s_2

-----WriteKafka.java-----*/
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class WriteKafka {
    private static void writeToKafka(String broker, String topic, String key, String message){
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, broker);
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.BATCH_SIZE_CONFIG, 16384);
        props.put(ProducerConfig.BUFFER_MEMORY_CONFIG, 33554432);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<>(props);
        producer.send(new ProducerRecord<>(topic, key, message));
        System.out.print("send");
        producer.close();
    }
}


