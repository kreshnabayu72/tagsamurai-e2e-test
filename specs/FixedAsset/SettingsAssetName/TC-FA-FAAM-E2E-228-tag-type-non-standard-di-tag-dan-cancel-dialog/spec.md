---
id: TC-FA-FAAM-E2E-228-tag-type-non-standard-di-tag-dan-cancel-dialog
title: "TAG Type Ber-Aset: Tag Bertipe Lama Menjadi Non-Standard di tag/ dan Cancel Dialog Tidak Mengubahnya"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-665
  - TC-FA-FAAM-828
coverage:
  web: automated
---

# TAG Type Ber-Aset: Tag Bertipe Lama Menjadi Non-Standard di tag/ dan Cancel Dialog Tidak Mengubahnya

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) dengan akses Fixed Asset > TAG. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup: No. 10 (`Dell Latitude`, Total Asset 42, TAG Type `RFID`+`QR`) dan No. 29 (Tag `Paired` pada aset `Dell Latitude`: sedikitnya satu aset ber-Tag `Paired` bertipe `RFID` dan satu bertipe `QR`; jumlah aset ber-Tag `RFID` dicatat sebagai `[N RFID]` oleh seed API). `Dell Latitude` tidak dapat digandakan dan menjadi target Edit TAG Type TC-FA-FAAM-828; hook `before` dan hook `after` serta langkah 25 menyediakannya ulang ke keadaan Pre-setup No. 10 dan No. 29 lewat seed API (kemampuan disediakan tim BE/FE). Efek: Last Updated `Dell Latitude` dan audit trail berubah; suite berjalan serial. Pernyataan ini belum ada di `suite.md` (lihat Temuan untuk QA).
- Kemampuan teknis: Fixed Asset > TAG > Paired (baris grup, kolom Non-standard, kartu `Non-standard`, kolom TAG Type, Popup Detail dengan ikon peringatan dan tooltip); seed API yang mengembalikan `[N RFID]`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan `Dell Latitude` ke Pre-setup No. 10 dan No. 29.
- State global yang diubah: TAG Type `Dell Latitude` (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-665 dan 828: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-665: Cancel pada dialog Change TAG Type tidak menjadikan Tag bertipe lama Non-standard

1. Buka Fixed Asset > TAG > Paired
2. Ketik Search `Dell Latitude`, tekan Enter
3. Catat Non-standard seluruh baris grup `Dell Latitude` sebagai nilai X
4. Buka Fixed Asset > Settings > Asset Master > Asset Name
5. Ketik Search `Dell Latitude`, tekan Enter
6. Klik `⋯` baris `Dell Latitude` lalu `Edit`
7. Lepas `RFID` dan pilih `NFC` pada TAG Type
8. Klik `[Save]`
9. Klik `[Cancel]` pada dialog Change TAG Type
10. Klik `✕` pada Modal Edit
11. Verifikasi dialog `Unsaved Changes`
12. Klik `[Leave]`
13. Buka Fixed Asset > TAG > Paired
14. Ketik Search `Dell Latitude`, tekan Enter
15. Verifikasi Non-standard seluruh baris grup `Dell Latitude` sama dengan nilai X pada langkah 3
16. Verifikasi kolom TAG Type baris grup tetap menampilkan icon `RFID` dan `QR`

### TC-FA-FAAM-828: Edit TAG Type langsung menjadikan Tag bertipe lama Non-standard di tab Paired

17. Catat Non-standard seluruh baris grup `Dell Latitude` sebagai nilai Y dan angka kartu `Non-standard` sebagai nilai K
18. Buka Fixed Asset > Settings > Asset Master > Asset Name
19. Ketik Search `Dell Latitude`, tekan Enter
20. Klik `⋯` baris `Dell Latitude` lalu `Edit`
21. Lepas `RFID` dan pilih `NFC` pada TAG Type
22. Klik `[Save]`
23. Klik `[Save]` pada dialog Change TAG Type
24. Buka lagi Fixed Asset > TAG > Paired tanpa tindakan lain
25. Ketik Search `Dell Latitude`, tekan Enter
26. Verifikasi Non-standard seluruh baris grup `Dell Latitude` bertambah `[N RFID]` dibanding nilai Y pada langkah 17, tanpa tindakan tambahan setelah Save
27. Verifikasi angka kartu `Non-standard` bertambah `[N RFID]` dibanding nilai K pada langkah 17
28. Verifikasi kolom TAG Type baris grup menampilkan icon `NFC` dan `QR`
29. Klik Asset Name `Dell Latitude` pada baris grup itu
30. Verifikasi Popup Detail menampilkan ikon peringatan di samping setiap Tag `RFID` dengan tooltip `This TAG type is not required by the asset name.`
31. Verifikasi ikon peringatan tidak tampil di samping Tag `QR`
32. Tutup Popup Detail
33. Sediakan ulang `Dell Latitude` ke keadaan Pre-setup No. 10 dan No. 29 lewat seed API

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 4, 13, 18, 24 (navigasi), langkah 2, 5, 14, 19, 25 (Search untuk menemukan baris target), langkah 3, 17 (mencatat baseline), langkah 10 dan 12 (menutup form dirty secara deterministik; S-08), langkah 32 (menutup Popup Detail), dan langkah 33 (pemulihan fixture; S-09).
- TC-FA-FAAM-665 tidak menyimpan perubahan (tidak ada pemulihan data); langkah 33 memulihkan keadaan setelah TC-FA-FAAM-828.
- Urutan TC: TC-FA-FAAM-665 (tidak menyimpan perubahan) sebelum TC-FA-FAAM-828 (menyimpan perubahan).
- Pembagian TC lintas spec: TC-FA-FAAM-829 ada di spec 245; TC-FA-FAAM-664 dan 838 ada di spec 229.
- Temuan untuk QA:
  - Post Condition TC-FA-FAAM-828 ("Tag RFID tetap berstatus `Paired`") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-FA-FAAM-665 tidak menyebut langkah penutupan form Edit setelah `[Cancel]`; spec menutup form dengan `✕` dan `[Leave]` (S-08) agar form dirty tidak terbawa.
  - TC-FA-FAAM-828 dan 665 mengubah/mengedit `Dell Latitude` (Pre-setup No. 10); S-06 mensyaratkan fixture pemulihan dinyatakan di `suite.md` (belum ada).
