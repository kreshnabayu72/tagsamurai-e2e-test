---
id: TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field
title: "Create User: Validasi Emoji First Name dan Last Name, Format Email, Temporary Until, dan Custom Field Emergency Phone"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-105
  - TC-GS-USER-106
  - TC-GS-USER-107
  - TC-GS-USER-108
  - TC-GS-USER-110
  - TC-GS-USER-111
  - TC-GS-USER-121
  - TC-GS-USER-122
  - TC-GS-USER-123
  - TC-GS-USER-124
  - TC-GS-USER-158
  - TC-GS-USER-159
coverage:
  web: automated
---

# Create User: Validasi Emoji First Name dan Last Name, Format Email, Temporary Until, dan Custom Field Emergency Phone

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data):
  - Master Data Division `Finance` (No. 23).
  - Custom Field aktif `Emergency Phone` (Phone) (No. 24); Required hanya aktif untuk TC-GS-USER-158, TC lain di spec ini dijalankan saat Required nonaktif.
  - Hendra Gunawan (Default User, No. 1), email `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net`; dipakai sebagai pembanding pembacaan user lewat backend.
- Data Dinamis: tidak ada user yang boleh tercipta; seluruh `[Submit]` diblokir validasi. Email uji yang valid memakai suffix `budisantoso+{runId}-022@qwertysystem.net` supaya pembacaan backend untuk Verifikasi "user tidak dibuat" tidak bertabrakan dengan data spec lain. Email berformat salah (`budisantoso.qwertysystem.net`, `budi@qwertysystem.n`) dipakai apa adanya karena input uji yang diblokir. Cleanup di hook `after`: hapus user ber-Email uji bila ada (cadangan bila validasi gagal dan user tercipta), tanpa mengandalkan hook `before` berhasil penuh.
- Data tanggal: "hari ini" dan "kemarin" pada Temporary Until dihitung dari Timezone client (General Settings client uji; NC-06), dibaca di hook `before` lewat kemampuan yang disediakan tim FE/BE. Spec tidak dijalankan mendekati pergantian hari 00.00 zona waktu client.
- State global yang diubah: status Required Custom Field `Emergency Phone` (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158). Required nonaktif sejak awal spec sampai sebelum TC-GS-USER-158, diaktifkan hanya untuk TC-GS-USER-158 (langkah 56; TC-GS-USER-159 tidak bergantung pada status Required), dan dipulihkan ke status awal di hook `after` walau spec gagal di tengah. Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal dan menonaktifkannya. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE bila belum ada):
  - Mengetik emoji dari keyboard dan menempel (paste) emoji dari clipboard ke field.
  - Menyuntikkan value langsung ke DOM field (melewati filter keystroke FE) dengan memicu event input sehingga validasi real-time berjalan; event yang dipicu ditentukan tim FE (TC tidak menyebutnya).
  - Membaca user menurut Email dari backend pada Client aktor (dipakai Verifikasi "user tidak dibuat"; endpoint tidak disebut di TC dan PRD).
  - Memilih tanggal pada field Temporary Until.

## Test Steps

### Pembukaan layar

1. Verifikasi pembacaan user lewat backend berfungsi: user Hendra Gunawan (Default User) ditemukan menurut Email
2. Klik `[+ User]` di Table Tools

### TC-GS-USER-105: Emoji diblok saat diketik dan di-paste di First Name

3. Ketik `Budi😊` di First Name
4. Verifikasi value First Name hanya `Budi`
5. Paste `🔥` ke First Name
6. Verifikasi value First Name tetap hanya `Budi`; emoji tidak pernah masuk field
7. Verifikasi tidak ada pesan error di First Name

### TC-GS-USER-106: Emoji di First Name yang lolos filter input ditolak validasi FE real-time

8. Klik `[Clear Field]`
9. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, pilih Access `Fixed Asset`, Emergency Phone `081234567890`
10. Injeksi value `Budi😊` langsung ke DOM field First Name (melewati filter keystroke FE)
11. Verifikasi inline error `First name contains invalid characters` muncul langsung di First Name tanpa menunggu `[Submit]`
12. Klik `[Submit]`
13. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-107: Emoji diblok saat diketik dan di-paste di Last Name

14. Klik `[Clear Field]`
15. Ketik `Budi😊` di Last Name
16. Verifikasi value Last Name hanya `Budi`
17. Paste `🔥` ke Last Name
18. Verifikasi value Last Name tetap hanya `Budi`; emoji tidak pernah masuk field
19. Verifikasi tidak ada pesan error di Last Name

### TC-GS-USER-108: Emoji di Last Name yang lolos filter input ditolak validasi FE real-time

20. Klik `[Clear Field]`
21. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, pilih Access `Fixed Asset`, Emergency Phone `081234567890`
22. Injeksi value `Budi😊` langsung ke DOM field Last Name (melewati filter keystroke FE)
23. Verifikasi inline error `Last name contains invalid characters` muncul langsung di Last Name tanpa menunggu `[Submit]`
24. Klik `[Submit]`
25. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-110: Format Email `budisantoso.qwertysystem.net` ditolak saat Submit

26. Klik `[Clear Field]`
27. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, pilih Access `Fixed Asset`, Emergency Phone `081234567890`
28. Isi Email `budisantoso.qwertysystem.net`
29. Klik `[Submit]`
30. Verifikasi inline error `Invalid email format` di Email
31. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso.qwertysystem.net` di backend

### TC-GS-USER-111: Format Email `budi@qwertysystem.n` ditolak saat Submit

32. Klik `[Clear Field]`
33. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, pilih Access `Fixed Asset`, Emergency Phone `081234567890`
34. Isi Email `budi@qwertysystem.n`
35. Klik `[Submit]`
36. Verifikasi inline error `Invalid email format` di Email
37. Verifikasi user tidak dibuat: tidak ada user ber-Email `budi@qwertysystem.n` di backend

### TC-GS-USER-121: Field Temporary Until muncul saat Set as Temporary User dicentang

38. Klik `[Clear Field]`
39. Centang `Set as Temporary User`
40. Verifikasi field `Temporary Until *` (placeholder `Select date`) muncul
41. Hapus centang `Set as Temporary User`
42. Verifikasi field `Temporary Until` hilang

### TC-GS-USER-122: Temporary Until kosong saat Temporary dicentang ditolak

43. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, pilih Access `Fixed Asset`, Emergency Phone `081234567890`
44. Centang `Set as Temporary User`, biarkan Temporary Until kosong
45. Klik `[Submit]`
46. Verifikasi inline error `Temporary until must not be empty`
47. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-123: Temporary Until hari ini ditolak

48. Pilih Temporary Until = hari ini (Timezone client)
49. Klik `[Submit]`
50. Verifikasi inline error `Please select a future date.`
51. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-124: Temporary Until kemarin ditolak

52. Ganti Temporary Until dengan kemarin (Timezone client)
53. Klik `[Submit]`
54. Verifikasi inline error `Please select a future date.`
55. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-158: Custom Field Required kosong ditolak saat Submit

56. Aktifkan status Required Custom Field `Emergency Phone` (kemampuan tim FE/BE, bukan aksi UI), lalu hapus centang `Set as Temporary User`
57. Klik `[Clear Field]`
58. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, pilih Access `Fixed Asset` (Emergency Phone kosong)
59. Klik `[Submit]`
60. Verifikasi inline error `Emergency phone must not be empty`
61. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-159: Custom Field Phone di bawah 4 digit ditolak real-time

62. Ketik `081` di Emergency Phone
63. Verifikasi inline error `Min. 4 characters` muncul langsung di Emergency Phone

### Penutup

64. Klik `✕` di header Popup
65. Verifikasi dialog `Unsaved Changes` tampil
66. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. TC-GS-USER-121 sampai 124 memakai Popup yang sama secara berantai (Temporary tetap tercentang dari TC-GS-USER-122 sampai 124); TC-GS-USER-158 menghapus centang Temporary lebih dulu supaya satu-satunya penyebab penolakan adalah Custom Field Required.
- Spec melewati sekitar 35 langkah (66 langkah) karena seluruh blok berada di satu kelas harness (validasi field Create yang diblokir, tanpa data tercipta), memakai satu layar dan satu pembukaan Popup dengan field dikosongkan di antara kasus (prinsip 13, halaman yang dipakai berulang), dan tiap blok berdiri sendiri. Jumlah langkah besar karena Expected dipecah per klausa (S-01).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): `[Clear Field]` di awal blok untuk membersihkan state antar-TC (S-03, S-09); menghapus centang `Set as Temporary User` sebelum TC-GS-USER-158; pengisian field wajib lain dan `Emergency Phone` `081234567890` pada TC-GS-USER-106, 108, 110, 111, 122 sampai 124 supaya satu-satunya penyebab penolakan adalah kasus yang diuji; pengaktifan Required di langkah 56 sebelum TC-GS-USER-158.
- Verifikasi pembacaan user Hendra Gunawan lewat backend di bagian Pembukaan layar adalah anchor positif untuk Verifikasi "user tidak dibuat" (8b butir 2); asersi tambahan ini tidak ada di TC dan dicatat sebagai pengecualian S-03.
- Penutup Popup memakai alur form dirty deterministik (`✕`, dialog `Unsaved Changes`, `[Leave]`) sesuai S-08; Verifikasi dialog di langkah penutup adalah prosedur penutupan, bukan Expected TC.
- Email uji memakai suffix `{runId}-022` karena Verifikasi "user tidak dibuat" membaca backend; nilai TC `budisantoso@qwertysystem.net` tidak diketik apa adanya.
- Temuan untuk QA:
  - TC-GS-USER-106, 108, 110, 111, 122, 123, 124 menyebut "user tidak dibuat" tanpa cara memeriksa; spec membaca backend menurut Email (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-105 dan 107 menyebut "Paste" tanpa mekanisme clipboard; TC-GS-USER-106 dan 108 menyebut "Injeksi value langsung ke DOM" tanpa event yang dipicu. Ditentukan tim FE di tahap script.
  - Tabel Pre-setup No. 24 menyatakan `Emergency Phone` Required hanya aktif untuk TC-GS-USER-158; TC-GS-USER-106, 108, 110, 111, 122, 123, 124 dijalankan saat Required nonaktif dan tidak mengisi Custom Field. Spec tetap mengisi `Emergency Phone` pada blok tersebut (sisa dari fix sebelumnya, tidak merugikan); TC tidak mewajibkannya.
  - TC-GS-USER-158 tidak menyebut cara mengaktifkan Required di tengah Popup yang sudah terbuka; spec mengaktifkannya di langkah 56 lewat kemampuan tim FE/BE. Bila perubahan Required hanya terbaca saat Popup dibuka ulang, tim FE menyesuaikan di tahap script.
  - TC-GS-USER-123 dan 124 mensyaratkan tanggal "hari ini" dan "kemarin" menurut zona waktu client (NC-06); TC tidak menyebut cara menghitungnya. Spec membaca Timezone client di hook `before`.
  - TC-GS-USER-123 mensyaratkan field Temporary Until dapat dipilih pada tanggal hari ini dan kemarin; bila date picker menonaktifkan tanggal lampau, kasus TC-GS-USER-124 tidak dapat dijalankan lewat picker. TC tidak menyebut perilaku picker.
  - TC-GS-USER-159 Expected hanya `Min. 4 characters`; TC tidak menyebut apakah error Required tampil bersamaan. Spec mengasersi hanya yang disebut.
