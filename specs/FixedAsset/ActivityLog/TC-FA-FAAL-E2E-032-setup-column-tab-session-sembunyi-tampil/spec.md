---
id: TC-FA-FAAL-E2E-032-setup-column-tab-session-sembunyi-tampil
title: "Setup Column Tab Session: Screening Overlay dan Popup, Sembunyi/Tampil Kolom, dan Kolom Terakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-107
  - TC-FA-FAAL-108
  - TC-FA-FAAL-109
  - TC-FA-FAAL-115
coverage:
  web: automated
---

# Setup Column Tab Session: Screening Overlay dan Popup, Sembunyi/Tampil Kolom, dan Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11), hanya dibaca dan tidak diubah. Spec ini mengasersi kolom dan Live Preview, bukan isi baris tertentu. Fixture `fixtures/activity-log.json` disediakan tim FE (nama kunci ditetapkan tim FE).
- Daftar 10 kolom Tab Session berurutan: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device/Browser.
- Kolom untuk langkah berulang (langkah 15 sampai 26; Data Uji TC-FA-FAAL-109):

  | Kolom |
  |---|
  | `Date` |
  | `User` |
  | `Employee ID` |
  | `Position` |
  | `Division` |
  | `Activity` |
  | `Status` |
  | `Note` |
  | `IP Address` |
  | `Device/Browser` |

- State yang diubah spec: konfigurasi kolom Tab Session (disimpan lewat `[Save]`). Langkah 26 mengembalikan tiap kolom ke tampil; hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-107: Screening Overlay Column Visibility Tab Session

1. Klik header kolom Actions (⋯)
2. Verifikasi overlay Column Visibility memuat 10 kolom urut: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device/Browser
3. Verifikasi semua checkbox kolom tercentang dan enabled
4. Verifikasi setiap baris kolom punya drag handle
5. Verifikasi item `Setup Column...` ada di bagian bawah overlay

### TC-FA-FAAL-108: Screening Popup Setup Column Tab Session

6. Klik `Setup Column...`
7. Verifikasi header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol close `(X)`
8. Verifikasi body memuat 10 kolom dengan checkbox tercentang
9. Verifikasi setiap kolom di body memiliki drag handle
10. Verifikasi setiap kolom di body memiliki icon Pin
11. Verifikasi Live Preview memiliki urutan header dan data sel sama dengan tabel
12. Verifikasi footer memuat tombol `[Reset to Default]` dan `[Save]` rata kanan
13. Verifikasi footer tidak memuat tombol `[Cancel]`
14. Klik `(X)` pada popup

### TC-FA-FAAL-109: Sembunyikan dan tampilkan kolom Tab Session lewat Popup Setup Column

Untuk setiap baris tabel Prerequisites "Kolom untuk langkah berulang" (langkah 15 sampai 26):

15. Klik header kolom Actions (⋯) > `Setup Column...`
16. Hilangkan centang kolom
17. Verifikasi kolom hilang dari Live Preview
18. Klik `[Save]`
19. Verifikasi kolom hilang dari tabel
20. Tekan F5
21. Verifikasi kolom tersisa pertama tampil di tabel setelah muat ulang
22. Verifikasi kolom tetap hilang dari tabel setelah muat ulang
23. Klik header kolom Actions (⋯) > `Setup Column...`
24. Centang kembali kolom
25. Klik `[Save]`
26. Verifikasi kolom tampil kembali di tabel

### TC-FA-FAAL-115: Kolom visible terakhir Tab Session tidak dapat disembunyikan

27. Klik header kolom Actions (⋯) > `Setup Column...`
28. Hilangkan centang sembilan kolom berurutan (Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address) hingga hanya Device/Browser tercentang
29. Arahkan kursor ke checkbox Device/Browser
30. Verifikasi checkbox Device/Browser disabled dengan tooltip `At least one column must remain visible.`
31. Coba hilangkan centang Device/Browser
32. Verifikasi Device/Browser tetap tercentang
33. Verifikasi Live Preview tetap memiliki satu kolom data
34. Klik `(X)` pada popup

## Notes

- Alasan di atas 35 langkah dengan ekspansi (34 langkah nominal; langkah 15 sampai 26 diulang untuk 10 kolom sehingga 142 langkah): keempat TC satu halaman, satu dataset #11, dan satu kelas fungsional (Setup Column), dan TC-FA-FAAL-109 satu TC dengan 10 iterasi yang tidak dapat dipecah (satu TC tetap satu spec); tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berulang mengikuti idiom "Untuk setiap baris tabel" (butir 8b.7); `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03): langkah 14 dan 34 (menutup popup tanpa Save, agar popup tidak terbawa ke TC berikutnya, S-09).
- Langkah 21 mengikuti butir a TC-FA-FAAL-109 ("kolom tersisa pertama tampil"): anchor bahwa halaman termuat setelah F5, ditulis sebelum `Verifikasi` kolom tetap hilang (butir 8b.2).
- Langkah 23 sampai 25 membuka kembali popup setelah muat ulang (urutan TC-FA-FAAL-109 langkah 3: "muat ulang halaman, buka Setup Column lagi dan centang kembali kolom, klik `[Save]`").
- Langkah 3 dan 4 memecah butir b Expected TC-FA-FAAL-107 per klausa (checkbox, drag handle; S-01); langkah 8 sampai 11 memecah butir Body TC-FA-FAAL-108 per klausa (checkbox, drag handle, icon Pin, Live Preview), sedangkan langkah 7 (header) dan langkah 12 (pasangan tombol footer) tetap satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-FAAL-115 Expected b menulis "tabel tetap memiliki satu kolom data", padahal tidak ada langkah `[Save]` sehingga tabel utama masih menampilkan 10 kolom; spec mengasersi Live Preview (langkah 33) yang mencerminkan keadaan popup.
  - TC-FA-FAAL-107, 108, 109, 115 mengasumsikan konfigurasi kolom awal adalah bawaan (10 kolom tampil, urutan bawaan, tanpa pin); spec mengandalkan preferensi kolom di browser yang bersih saat spec dimulai (pemulihan oleh hook `after` spec yang menyimpan konfigurasi kolom, kemampuan disediakan tim FE).
  - TC-FA-FAAL-109 menulis "muat ulang halaman" tanpa menyebut cara; spec memakai F5.
