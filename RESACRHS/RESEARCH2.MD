# 1

## Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin

Interpreter diller yorumlayıcı dillərdir, bu dillər sizin yazdığınız kodları bir-başa olaraq maşın yorumlayaraq izah edir.  Java Python PHP və başqa dillər

# 2

## Interpreted və compiler dillər arasında olan fərqləri izah edin

Complier dillər isə dərləyici dillərə deyilir. Bu tip dillər yazdığı kodu ilk olaraq başqa bir dilə və ya maşına dərləyir. Complier dillərə misal olaraq C C++ misal gətirmək olar. Complier və İnterperter dillərin əsas fərqi isə Complier dillərin daha sürətli olmasıdır çünki İnterpreter dillər yorumlama işləminin hər dəfəsində təkrar edir amma Complier dillər isə bunu bir dəfə təkrar edir ona görə də complier dillər daha sürətlidir.

# 3

## Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin

- Integer (Integer tam ədədləri tanımlamaq üçün istifadə olunur)
- Float (Float tam ədədləri tanımlamaq üçün istifadə olunur)
- Strings (Yazı tiplərini tanımlamaq üçün istifadə olunur, burda yazılar dırnaq içərisində yazılır və dırnaq içərisində yazılan rəqəm belə yazı sayılır)
- List (Birdən daha çox dəyişkənin tanımlanması üçün kömək edən data typedir, bu metodda dəyişkənlərimiz müxtəlif ola bilər yəni float integer string və s)
- Dictionaries (Birdən daha çox stringləri tanımlamaq üçün istifadə olunur burda bir key və onun qiyməti olur yəni ("name:" "Elmir") Bu formada)
- Booleans (Bu qaydalı olaraq 2 qiyməti var true və ya false)
- Set (birdən daha çox sırası stringi tanımlamaq üçün istifadə olunur)


# 4

## Object Oriented Programming nədir? Niyə belə bir paradigmanın var olduğunu izah edin
 
- OOP yəni Object Oriented Programming obje əsaslı programlama dilidir. Yəni bu dildə hər bir şey bir obje kimi götürülür (Əşya canlı və s). Bunun əsas üstünlüyü bu dildə anlaşıqlılığın daha yüksək olmasıdır yəni siz bir şey daha rahaqlıla başa sala bilirsiniz. 

# 5

## Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?

-   

# 6

## local və global variable nədir izah edin

- Local variable müəyyən bir kod içində olar alt variablelərdir və kod bitdikdən sonra yox olurlar buna məsələn 
public int add(){
int a =4;
int b=5;
return a+b;
}
Burda a və b local variablelərdir.

- Global variablelər isə əvvəlində tanımlanmış və program bitənə kimi o qiymətləri özündə saxlayan variblelərdir.

int a =4;
int b=5;
public int add(){
return a+b;
}

# 7

## Python type conversion haqqında izahat verin

- Pythonda 2 cür type conversion  vardır(Implicit Type Conversion və Explicit Type Conversion)

- İmplicit - dönüştürmədə interperter bir data typeni avtomatik olaraq digərinə dönüşdürür. Məsələn 
    (
        x = 10

    print("x is of type:",type(x))

    y = 10.6
    print("y is of type:",type(y))

    x = x + y

    print(x)
    print("x is of type:",type(x))
    )
Burda avtomatik olaraq x - i integer edib sonra isə floata dönüşdürdü.

- Explicit Type Conversion 

# 8 

## init nədir?

- İnit Linuxlar üçün önəmli bir koddur bu bur çox programa başlamadan əvvəl girilən bir koddur

# 9

## Self nedir? 

- Selfin yazılması sizin yazdığlnız class aid olan parametrləri istifadə edəcəyin mənasına gəlir.

# 10

## *args,**kwargs nədir? nə zaman istifadə olunur?

- *args (Biz bir class 256 parametrə vermək istədikdə ona bəzi funksiyaları əvvəlcədən verməliyik məsələn qarşısını * işarəsi qoyaraq) 

- **kvargs (Biz classı çağıransa onu key value görə çağıra bilərik bunun üçün əvvəlcədən function qarşısında ** işarəsi qoymaq lazıçdır)

# 11

## Python module nədir?

- modullar bəzi işləri rahatlıqla edə biləcəyimiz funksiyaları bəzi dəyərləri özündə saxlayan toollardır

### Moudllar iki yerə bölünür

-  Hazır Modullar
-  Öz hazırladığımız modullar

# 12

## Python package nədir?


