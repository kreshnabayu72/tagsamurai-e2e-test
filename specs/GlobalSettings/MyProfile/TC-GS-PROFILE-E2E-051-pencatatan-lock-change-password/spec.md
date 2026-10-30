---
id: TC-GS-PROFILE-E2E-051-pencatatan-lock-change-password
title: "Pencatatan Change Password: Note Locked 15 Menit, 1 Jam, Wajib Reset, dan Eskalasi 7 Hari"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-232
  - TC-GS-PROFILE-233
  - TC-GS-PROFILE-234
  - TC-GS-PROFILE-235
coverage:
  web: automated
---

# Pencatatan Change Password: Note Locked 15 Menit, 1 Jam, Wajib Reset, dan Eskalasi 7 Hari

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #7 (Maya Anggraini, Total Control, password aktif `Passw0rd!Old`, Time Format 24 jam) `passwordProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Pembaca log: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, login lewat UI pada langkah ganti akun.
- Env var: `GS_PROFILE_PWD_PASSWORD`, `PROFILE_PASSWORD_NEW` (Data Dinamis #3, `N3wPassw0rd!`), `GS_PROFILE_ADMIN_PASSWORD`.
- Input uji Current Password salah `Wr0ngPass!` ditulis literal seperti di TC: masukan uji yang ditolak server, bukan kredensial akun.
- State awal tiap tier (diatur lewat fixture BE yang disediakan tim FE/BE setelah reset hook `beforeEach`; mekanisme tidak disebut TC, PRD, atau LLD):

  | TC | Counter Change Password | State tahap | Note yang diharapkan |
  |---|---|---|---|
  | TC-GS-PROFILE-232 | 2 | belum terkunci | `Locked 15 minutes (change password)` |
  | TC-GS-PROFILE-233 | 5 | tahap 15 menit sudah lewat | `Locked 1 hour (change password)` |
  | TC-GS-PROFILE-234 | 8 | tahap 1 jam sudah lewat | `Locked requires reset (change password)` |
  | TC-GS-PROFILE-235 | tujuh hari berturut-turut mencapai lock 1 jam | - | `Account locked (change password)` |

- Jam: bila fixture state tahap menggeser jam server, jam server dipulihkan (langkah 17) sebelum admin membuka User Log atau Activity Log (S-09). Log yang dibuat saat jam digeser dicari berdasarkan Note, bukan posisi "teratas" (S-12).
- Kemampuan baca baseline: jumlah baris Activity `Change Password` per Note pada Tab User Log Detail Maya Anggraini dan pada Activity Log > Session sebelum aksi (S-12; disediakan tim FE/BE).
- Pemulihan (R-08): langkah 17 memulihkan jam server dan counter Change Password Maya Anggraini ke 0 lewat fixture BE; hook `after` suite memulihkan state yang sama bila spec gagal di tengah.
- State global yang diubah: counter dan state lock Pre-setup #7, jam server (bila dipakai fixture). Suite berjalan serial (`parallel: false`).

## Test Steps

### Aksi pemicu lock per tier

1. Catat baseline lewat kemampuan baca: jumlah baris Activity `Change Password` per Note pada tabel Prerequisites di Tab User Log Detail Maya Anggraini dan pada Activity Log > Session
2. Untuk setiap baris TC-GS-PROFILE-232 sampai TC-GS-PROFILE-234 pada tabel Prerequisites (langkah 3 sampai 9)
3. Atur counter dan state tahap Change Password Maya Anggraini sesuai baris tabel lewat fixture BE
4. Klik `[Change Password]`
5. Isi Current Password `Wr0ngPass!`, New Password `N3wPassw0rd!`, Confirm New Password `N3wPassw0rd!`
6. Klik `[Save]`
7. Klik `✕`
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`

### TC-GS-PROFILE-235: Eskalasi 7 hari

10. Atur state tujuh hari berturut-turut mencapai lock 1 jam pada counter Change Password Maya Anggraini lewat fixture BE
11. Klik `[Change Password]`
12. Isi Current Password `Wr0ngPass!`, New Password `N3wPassw0rd!`, Confirm New Password `N3wPassw0rd!`
13. Klik `[Save]`
14. Klik `✕`
15. Verifikasi dialog `Unsaved Changes` tampil
16. Klik `[Leave]`
17. Pulihkan jam server dan counter Change Password Maya Anggraini ke 0 lewat fixture BE
18. Logout
19. Login sebagai admin Hendra Wijaya (Pre-setup #6)

### Pembacaan User Log dan Activity Log > Session

20. Buka Global Settings > User > Detail Maya Anggraini > Tab User Log
21. Verifikasi TC-GS-PROFILE-232: Tab User Log memuat baris baru Activity `Change Password`, Status `Failed`, Note `Locked 15 minutes (change password)` (jumlah baris dengan Note itu bertambah tepat satu dibanding baseline)
22. Verifikasi TC-GS-PROFILE-233: Tab User Log memuat baris baru Activity `Change Password`, Status `Failed`, Note `Locked 1 hour (change password)` (jumlah baris dengan Note itu bertambah tepat satu dibanding baseline)
23. Verifikasi TC-GS-PROFILE-234: Tab User Log memuat baris baru Activity `Change Password`, Status `Failed`, Note `Locked requires reset (change password)` (jumlah baris dengan Note itu bertambah tepat satu dibanding baseline)
24. Verifikasi TC-GS-PROFILE-235: Tab User Log memuat baris baru Activity `Change Password`, Status `Failed`, Note `Account locked (change password)` (jumlah baris dengan Note itu bertambah tepat satu dibanding baseline)
25. Buka Global Settings > Activity Log > Session
26. Verifikasi TC-GS-PROFILE-232: Activity Log > Session memuat baris baru untuk Maya Anggraini Activity `Change Password`, Status `Failed`, Note `Locked 15 minutes (change password)`
27. Verifikasi TC-GS-PROFILE-233: Activity Log > Session memuat baris baru untuk Maya Anggraini Activity `Change Password`, Status `Failed`, Note `Locked 1 hour (change password)`
28. Verifikasi TC-GS-PROFILE-234: Activity Log > Session memuat baris baru untuk Maya Anggraini Activity `Change Password`, Status `Failed`, Note `Locked requires reset (change password)`

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness d (counter dan jam server lewat fixture). Langkah 2 sampai 9 diulang untuk tiga baris tabel Prerequisites (parameter tiap iterasi di tabel); `Verifikasi` dialog `Unsaved Changes` ditulis sekali per iterasi. Ekspansi: 7 langkah x 3 + 7 langkah TC-GS-PROFILE-235 + 5 langkah pembuka dan penutup + 9 langkah baca-log.
- Spec melewati sekitar 35 langkah menurut ekspansi karena empat TC berada dalam satu kelas (pencatatan lock, satu akun, satu kali pembacaan log oleh admin) dan membaca log sekali di akhir menghindari ganti akun berulang; kegagalan satu tier tidak membuat tier lain kehilangan makna karena tiap tier mengatur state-nya sendiri. Blok baca-log berpola (langkah 20 sampai 28) tidak dihitung menurut bagian 3.
- Pembagian TC: TC-GS-PROFILE-235 hanya diasersi di Tab User Log sesuai Expected TC; tidak diasersi di Activity Log > Session.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 sampai 9 dan 14 sampai 16 (menutup modal dirty lewat `✕`, dialog `Unsaved Changes`, `[Leave]`, S-08), 17 (pemulihan jam server dan counter sebelum admin membaca log, S-09).
- Temuan untuk QA:
  - TC-GS-PROFILE-233 dan 234 menulis "tahap 15 menit sudah lewat" dan "tahap 1 jam sudah lewat" sebagai precondition tanpa cara menyiapkannya; spec menuliskannya sebagai state fixture BE yang disediakan tim FE/BE.
  - TC-GS-PROFILE-235 menyebut "tujuh hari berturut-turut mencapai lock 1 jam (fixture BE)" tanpa rincian state; spec mengikuti TC dan menuliskannya sebagai state fixture.
  - TC-GS-PROFILE-232 sampai 235 tidak menyebut Expected untuk toast atau tampilan modal setelah penolakan; spec hanya mengasersi baris log sesuai Expected dan menutup modal dirty deterministik.
