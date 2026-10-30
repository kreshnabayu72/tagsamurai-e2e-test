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
  - Custom Field aktif `Emergency Phone` (Phone, Required) (No. 24).
  - Hendra Gunawan (Default User, No. 1), email `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net`; dipakai sebagai pembanding pembacaan user lewat backend.
- Data Dinamis: tidak ada user yang boleh tercipta; seluruh `[Submit]` diblokir validasi. Email uji yang valid memakai suffix `budisantoso+{runId}-022@qwertysystem.net` supaya pembacaan backend untuk Verifikasi "user tidak dibuat" tidak bertabrakan dengan data spec lain. Email berformat salah (`budisantoso.qwertysystem.net`, `budi@qwertysystem.n`) dipakai apa adanya karena input uji yang diblokir. Cleanup di hook `after`: hapus user ber-Email uji bila ada (cadangan bila validasi gagal dan user tercipta), tanpa mengandalkan hook `before` berhasil penuh.
- Data tanggal: "hari ini" dan "kemarin" pada Temporary Until dihitung dari Timezone client (General Settings client uji; NC-06), dibaca di hook `before` lewat kemampuan yang disediakan tim FE/BE. Spec tidak dijalankan mendekati pergantian hari 00.00 zona waktu client.
- State global yang diubah: tidak ada. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE bila belum ada):
  - Mengetik emoji dari keyboard dan menempel (paste) emoji dari clipboard ke field.
  - Menyuntikkan value langsung ke DOM field (melewati filter keystroke FE) dengan memicu event input sehingga validasi real-time berjalan; event yang dipicu ditentukan tim FE (TC tidak menyebutnya).
  - Membaca user menurut Email dari backend pada Client aktor (dipakai Verifikasi "user tidak dibuat"; endpoint tidak disebut di TC dan PRD).
  - Memilih tanggal pada field Temporary Until.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Verifikasi pembacaan user lewat backend berfungsi: user Hendra Gunawan (Default User) ditemukan menurut Email
3. Klik `[+ User]` di Table Tools

### TC-GS-USER-105: Emoji diblok saat diketik dan di-paste di First Name

4. Ketik `Budi😊` di First Name
5. Verifikasi value First Name hanya `Budi`
6. Paste `🔥` ke First Name
7. Verifikasi value First Name tetap hanya `Budi`; emoji tidak pernah masuk field
8. Verifikasi tidak ada pesan error di First Name

### TC-GS-USER-106: Emoji di First Name yang lolos filter input ditolak validasi FE real-time

9. Klik `[Clear Field]`
10. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
11. Injeksi value `Budi😊` langsung ke DOM field First Name (melewati filter keystroke FE)
12. Verifikasi inline error `First name contains invalid characters` muncul langsung di First Name tanpa menunggu `[Submit]`
13. Klik `[Submit]`
14. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-107: Emoji diblok saat diketik dan di-paste di Last Name

15. Klik `[Clear Field]`
16. Ketik `Budi😊` di Last Name
17. Verifikasi value Last Name hanya `Budi`
18. Paste `🔥` ke Last Name
19. Verifikasi value Last Name tetap hanya `Budi`; emoji tidak pernah masuk field
20. Verifikasi tidak ada pesan error di Last Name

### TC-GS-USER-108: Emoji di Last Name yang lolos filter input ditolak validasi FE real-time

21. Klik `[Clear Field]`
22. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
23. Injeksi value `Budi😊` langsung ke DOM field Last Name (melewati filter keystroke FE)
24. Verifikasi inline error `Last name contains invalid characters` muncul langsung di Last Name tanpa menunggu `[Submit]`
25. Klik `[Submit]`
26. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-110: Format Email `budisantoso.qwertysystem.net` ditolak saat Submit

27. Klik `[Clear Field]`
28. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
29. Isi Email `budisantoso.qwertysystem.net`
30. Klik `[Submit]`
31. Verifikasi inline error `Invalid email format` di Email
32. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso.qwertysystem.net` di backend

### TC-GS-USER-111: Format Email `budi@qwertysystem.n` ditolak saat Submit

33. Klik `[Clear Field]`
34. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
35. Isi Email `budi@qwertysystem.n`
36. Klik `[Submit]`
37. Verifikasi inline error `Invalid email format` di Email
38. Verifikasi user tidak dibuat: tidak ada user ber-Email `budi@qwertysystem.n` di backend

### TC-GS-USER-121: Field Temporary Until muncul saat Set as Temporary User dicentang

39. Klik `[Clear Field]`
40. Centang `Set as Temporary User`
41. Verifikasi field `Temporary Until *` (placeholder `Select date`) muncul
42. Hapus centang `Set as Temporary User`
43. Verifikasi field `Temporary Until` hilang

### TC-GS-USER-122: Temporary Until kosong saat Temporary dicentang ditolak

44. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, centang Access `Fixed Asset`, Emergency Phone `081234567890`
45. Centang `Set as Temporary User`, biarkan Temporary Until kosong
46. Klik `[Submit]`
47. Verifikasi inline error `Temporary until must not be empty`
48. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-123: Temporary Until hari ini ditolak

49. Pilih Temporary Until = hari ini (Timezone client)
50. Klik `[Submit]`
51. Verifikasi inline error `Please select a future date.`
52. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-124: Temporary Until kemarin ditolak

53. Ganti Temporary Until dengan kemarin (Timezone client)
54. Klik `[Submit]`
55. Verifikasi inline error `Please select a future date.`
56. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-158: Custom Field Required kosong ditolak saat Submit

57. Hapus centang `Set as Temporary User`
58. Klik `[Clear Field]`
59. Isi First Name `Budi`, Last Name `Santoso`, Division `Finance`, Email `budisantoso+{runId}-022@qwertysystem.net`, centang Access `Fixed Asset` (Emergency Phone kosong)
60. Klik `[Submit]`
61. Verifikasi inline error `Emergency phone must not be empty`
62. Verifikasi user tidak dibuat: tidak ada user ber-Email `budisantoso+{runId}-022@qwertysystem.net` di backend

### TC-GS-USER-159: Custom Field Phone di bawah 4 digit ditolak real-time

63. Ketik `081` di Emergency Phone
64. Verifikasi inline error `Min. 4 characters` muncul langsung di Emergency Phone

### Penutup

65. Klik `✕` di header Popup
66. Verifikasi dialog `Unsaved Changes` tampil
67. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. TC-GS-USER-121 sampai 124 memakai Popup yang sama secara berantai (Temporary tetap tercentang dari TC-GS-USER-122 sampai 124); TC-GS-USER-158 menghapus centang Temporary lebih dulu supaya satu-satunya penyebab penolakan adalah Custom Field Required.
- Spec melewati sekitar 35 langkah (67 langkah) karena seluruh blok berada di satu kelas harness (validasi field Create yang diblokir, tanpa data tercipta), memakai satu layar dan satu pembukaan Popup dengan field dikosongkan di antara kasus (prinsip 13, halaman yang dipakai berulang), dan tiap blok berdiri sendiri. Jumlah langkah besar karena Expected dipecah per klausa (S-01).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): `[Clear Field]` di awal blok untuk membersihkan state antar-TC (S-03, S-09); menghapus centang `Set as Temporary User` sebelum TC-GS-USER-158; pengisian field wajib lain dan `Emergency Phone` `081234567890` pada TC-GS-USER-106, 108, 110, 111, 122 sampai 124 supaya satu-satunya penyebab penolakan adalah kasus yang diuji.
- Verifikasi pembacaan user Hendra Gunawan lewat backend di bagian Pembukaan layar adalah anchor positif untuk Verifikasi "user tidak dibuat" (8b butir 2); asersi tambahan ini tidak ada di TC dan dicatat sebagai pengecualian S-03.
- Penutup Popup memakai alur form dirty deterministik (`✕`, dialog `Unsaved Changes`, `[Leave]`) sesuai S-08; Verifikasi dialog di langkah penutup adalah prosedur penutupan, bukan Expected TC.
- Email uji memakai suffix `{runId}-022` karena Verifikasi "user tidak dibuat" membaca backend; nilai TC `budisantoso@qwertysystem.net` tidak diketik apa adanya.
- Temuan untuk QA:
  - TC-GS-USER-106, 108, 110, 111, 122, 123, 124 menyebut "user tidak dibuat" tanpa cara memeriksa; spec membaca backend menurut Email (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-105 dan 107 menyebut "Paste" tanpa mekanisme clipboard; TC-GS-USER-106 dan 108 menyebut "Injeksi value langsung ke DOM" tanpa event yang dipicu. Ditentukan tim FE di tahap script.
  - Tabel Pre-setup No. 24 mendefinisikan `Emergency Phone` Required, tetapi TC-GS-USER-106, 108, 110, 111, 122, 123, 124 tidak mengisi Custom Field; tanpa pengisian, `[Submit]` ditolak juga oleh Custom Field Required sehingga Verifikasi "user tidak dibuat" tidak dapat dibedakan penyebabnya. Spec mengisi `Emergency Phone` pada blok tersebut.
  - TC-GS-USER-123 dan 124 mensyaratkan tanggal "hari ini" dan "kemarin" menurut zona waktu client (NC-06); TC tidak menyebut cara menghitungnya. Spec membaca Timezone client di hook `before`.
  - TC-GS-USER-123 mensyaratkan field Temporary Until dapat dipilih pada tanggal hari ini dan kemarin; bila date picker menonaktifkan tanggal lampau, kasus TC-GS-USER-124 tidak dapat dijalankan lewat picker. TC tidak menyebut perilaku picker.
  - TC-GS-USER-159 Expected hanya `Min. 4 characters`; TC tidak menyebut apakah error Required tampil bersamaan. Spec mengasersi hanya yang disebut.
