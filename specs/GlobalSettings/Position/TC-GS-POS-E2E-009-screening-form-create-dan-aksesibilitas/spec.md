---
id: TC-GS-POS-E2E-009-screening-form-create-dan-aksesibilitas
title: Screening form Create dan aksesibilitas
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-10
  - TC-GS-POS-11
  - TC-GS-POS-12
  - TC-GS-POS-38
coverage:
  web: automated
---

# Screening form Create dan aksesibilitas

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.modal.create.title` adalah judul modal Create Position,
  yaitu `Create Position`.
- `Fixture.globalSettingsPosition.captions.form.label.positionName` adalah label field, yaitu
  `Position Name *`.
- `Fixture.globalSettingsPosition.captions.form.placeholder.positionName` adalah placeholder input,
  yaitu `Enter position name`.
- `Fixture.globalSettingsPosition.captions.form.checkbox.stayOnForm` adalah label checkbox, yaitu
  `Stay on this form after submitting`.
- `Fixture.globalSettingsPosition.captions.form.actions.submit` adalah label tombol submit, yaitu
  `Submit`.
- `Fixture.globalSettingsPosition.captions.form.actions.clearField` adalah label tombol reset, yaitu
  `Clear Field`.
- `Fixture.globalSettingsPosition.form.create.spec.maxLength` adalah batas karakter yang dibaca dari
  atribut `maxlength` pada input Name, dan nilainya harus 120 sesuai PRD §9.9. Nilai ini dibaca dari
  DOM, bukan ditulis di spec, supaya spec tidak ikut asserting angka yang keliru dua kali.
- `Fixture.globalSettingsPosition.form.create.hoverTarget` adalah nama Position valid untuk menguji
  feedback tombol, yaitu `Hover Test Create`. Namanya diambil dari fixture agar tidak bentrok dengan
  spec lain yang memakai nilai yang sama.
- Modal Create yang diuji hanya punya satu field isian dan satu checkbox. Verifikasi bahwa tidak ada
  field lain sengaja ada, karena wireframe PRD §4.2c menetapkan susunan itu dan field tambahan yang
  tidak terduga akan lolos kalau spec ini hanya memeriksa field yang diharapkan.
- Footer modal Create hanya boleh punya dua tombol. PRD §4.4 ayat 2 melarang menyandingkan `[Cancel]`
  bersama `[Clear Field]`, jadi keberadaan tombol ketiga di footer adalah pelanggaran yang harus
  terdeteksi di sini, bukan di spec lain.

## Test Steps

### Struktur tiga zona modal Create

1. Klik tombol `[+ Position]` di TableTools toolbar
2. Verifikasi modal dengan judul
   `Fixture.globalSettingsPosition.captions.modal.create.title` muncul di atas tabel
3. Verifikasi area di luar modal terhalang overlay gelap
4. Verifikasi tabel di belakang modal tidak dapat difokuskan dengan klik langsung
5. Verifikasi zona Header memuat judul modal dan icon close `[✕]`
6. Verifikasi zona Form Content memuat tepat dua elemen isian, yaitu field Name dan checkbox
   `Fixture.globalSettingsPosition.captions.form.checkbox.stayOnForm`
7. Verifikasi zona Footer Actions berada di sisi kanan dan memuat tepat dua tombol, yaitu
   `Fixture.globalSettingsPosition.captions.form.actions.clearField` dan
   `Fixture.globalSettingsPosition.captions.form.actions.submit`
8. Verifikasi tidak ada tombol `[Cancel]` di footer modal, sesuai PRD §4.4 ayat 2
9. Verifikasi tidak ada elemen isian lain selain field Name dan checkbox tersebut
10. Verifikasi field Name tampil sebagai input teks satu baris, bukan textarea
11. Verifikasi field Name menampilkan label
    `Fixture.globalSettingsPosition.captions.form.label.positionName`
12. Verifikasi tanda bintang pada label Name menandakan field wajib
13. Verifikasi field Name menampilkan placeholder
    `Fixture.globalSettingsPosition.captions.form.placeholder.positionName`
14. Verifikasi checkbox `Stay on this form after submitting` tampil dalam keadaan tidak tercentang
    sebagai kondisi awal
15. Verifikasi field Name kosong pada kondisi awal

### Aksesibilitas field Name

16. Verifikasi atribut `aria-required` pada field Name bernilai `true`, sesuai PRD §4.5
17. Verifikasi field Name terhubung ke pesan error melalui atribut `aria-describedby`, sehingga
    pembaca layar membacakan error bersama nama field
18. Verifikasi atribut `aria-required` juga tercermin pada tampilan, yaitu field ditandai wajib
19. Verifikasi input Name punya nama yang dapat diakses, bukan hanya rely pada label visual
20. Verifikasi field Name punya atribut `maxlength` yang sama dengan
    `Fixture.globalSettingsPosition.form.create.spec.maxLength`

### Fokus otomatis dan focus trap

21. Verifikasi kursor fokus otomatis berada di field Name sejak modal terbuka, sesuai PRD §4.5
22. Verifikasi tidak ada elemen di luar modal yang bisa difokuskan selama modal terbuka
23. Tekan tombol `Tab` berulang kali sampai seluruh elemen di dalam modal sudah dilewati
24. Verifikasi fokus hanya pernah berada pada elemen-elemen di dalam modal
25. Verifikasi tidak ada satu pun dari elemen itu fokusnya berada pada elemen di luar modal
26. Verifikasi setelah satu putaran Tab penuh, fokus kembali ke elemen pertama di dalam modal
27. Tekan tombol `Esc`
28. Verifikasi modal Create tertutup
29. Verifikasi tidak ada dialog Unsaved Changes yang muncul, karena pada langkah ini form belum
    diisi sehingga tidak dirty
30. Verifikasi fokus kembali ke tombol `[+ Position]` di halaman utama
31. Verifikasi tabel Position kembali dapat difokuskan dan diklik

### Feedback tombol Submit dan Clear Field

32. Klik tombol `[+ Position]` untuk membuka modal Create
33. Arahkan kursor ke tombol `Fixture.globalSettingsPosition.captions.form.actions.submit` pada
    kondisi form kosong
34. Verifikasi tombol Submit menampilkan state hover
35. Arahkan kursor ke tombol `Fixture.globalSettingsPosition.captions.form.actions.clearField` pada
    kondisi form kosong
36. Verifikasi tombol Clear Field menampilkan state hover
37. Verifikasi state hover kedua tombol berbeda dari warna latar saat pointer dilepas
38. Verifikasi tombol Clear Field tampil dengan variant text, bukan filled
39. Verifikasi tombol Submit tampil dengan variant filled
40. Verifikasi tombol Clear Field tidak sama visual dengan tombol Submit, sehingga tidak terlihat
    seperti dua tombol aksi utama
41. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.hoverTarget`
42. Klik tombol `Fixture.globalSettingsPosition.captions.form.actions.submit`
43. Verifikasi toast sukses muncul
44. Verifikasi baris `Fixture.globalSettingsPosition.form.create.hoverTarget` masuk ke tabel

## Notes

- Spec ini sengaja dipisah dari spec 010 yang menguji validasi dan dirty detection. Yang di sini
  hanya bentuk dan perilaku aksesibilitas modal saat masih kosong.
- Langkah 8 memeriksa tidak adanya tombol Cancel. Ini aturan eksplisit PRD §4.4 ayat 2 yang melarang
  penambahan Cancel di footer, dan kalau tidak diperiksa di sini, tidak akan terlihat kalau tim FE
  menambahkannya di kemudian hari.
- Langkah 9 memeriksa tidak adanya field tambahan. Pemeriksaan "field yang diharapkan ada" saja akan
  tetap lulus kalau ada field ekstra yang tidak dispesifikasikan di wireframe.
- Fokus otomatis pada langkah 21 dan focus trap pada langkah 23 sampai 26 dipecah terpisah karena
  keduanya punya sumber bug yang berbeda. Fokus otomatis bisa hilang karena refactor komponen,
  sedangkan focus trap hilang karena penanganan navigasi keyboard.
- Langkah 26 diperlukan karena focus trap yang salah bisa membuat fokus keluar ke elemen di belakang
  modal, bukan hanya berhenti di dalam. Tanpa pemeriksaan putaran penuh, bug baru terlihat saat
  pengguna menekan tombol Tab berulang banyak kali.
- Verifikasi fokus kembali ke tombol `[+ Position]` pada langkah 30 diuji karena memengaruhi
  pengalaman keyboard. Tanpa itu, pengguna yang menutup modal akan kehilangan posisinya di tabel.
- Langkah 21 sampai 30 sengaja dijalankan sebelum Pengisian apa pun supaya tidak bercampur dengan
  Dialog Unsaved Changes yang diuji di spec 010.
