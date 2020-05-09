from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = (
            'id', 'first_name', 'last_name', 'email', 'qualification', 'university', 'password', 'confirm_password',)

        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def create(self, validated_data):
        student = models.Student(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            qualification=validated_data['qualification'],
            university=validated_data['university'],
            password=validated_data['password'],
            confirm_password=validated_data['confirm_password'],

        )

        p1 = self.validated_data['password']
        p2 = self.validated_data['confirm_password']
        min_length = 8
        if p1 and p2:
            if p1 != p2:
                raise serializers.ValidationError('password is not matched with confirm password')
            if len(p1) < min_length:
                raise serializers.ValidationError('password must minimum 8 characters')
            if p1.isdigit():
                raise serializers.ValidationError("password should not only numeric")

        student.set_password(validated_data['password'])
        student.save()
        return student


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User

        exclude = ('last_login',)
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def create(self, validated_data, ):
        librarian = models.User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            confirm_password=validated_data['confirm_password'],

        )
        p1 = self.validated_data['password']
        p2 = self.validated_data['confirm_password']
        min_length = 8
        if p1 and p2:

            if p1 != p2:
                raise serializers.ValidationError('password does not match')
            else:
                if len(p1) < min_length:
                    raise serializers.ValidationError("password must minimum 8 characters ")
                if p1.isdigit():
                    raise serializers.ValidationError("password should not all numeric")

        librarian.set_password(validated_data['password'])
        librarian.save()
        return librarian
