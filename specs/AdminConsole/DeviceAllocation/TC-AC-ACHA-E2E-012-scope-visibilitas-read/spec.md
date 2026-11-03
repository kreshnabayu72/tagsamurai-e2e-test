---
id: TC-AC-ACHA-E2E-012-scope-visibilitas-read
title: "Scope Visibilitas READ List per Tipe Entitas (Principal, Distributor, Partner)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-71
  - TC-AC-ACHA-72
  - TC-AC-ACHA-73
  - TC-AC-ACHA-74
  - TC-AC-ACHA-75
coverage:
  web: automated
---

# Scope Visibilitas READ List per Tipe Entitas (Principal, Distributor, Partner)

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

| TC | Entitas | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-71 | Total Control Principal PT ABC | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-72, TC-73, TC-75 | Total Control Distributor PT Global Distribusi | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| TC-74 | Total Control Partner CV Mitra Solusi | #43 | `totalControlPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P1_PASSWORD` |

- Login akun aktor pertama (Principal) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Seed 30 alokasi (Pre-setup #48) dengan pengirim PT ABC, PT Global Distribusi, CV Mitra Solusi, dan PT Nusa Distribusi serta Client PT Sejahtera Logistik, PT Retail Makmur, PT Manufaktur Unggul, PT Bintang Timur. Jumlah baris per scope diturunkan dari seeding: Principal 30 baris (10, 10, 10), Distributor PT Global Distribusi 22 baris (16 dikirim PT Global Distribusi dan 6 ke Client dalam jaringannya; 10, 10, 2), Client PT Retail Makmur oleh Distributor 6 baris, Partner CV Mitra Solusi 6 baris. Fixture baseline memulihkan seed ke keadaan awal sebelum spec dijalankan.
- Kemampuan teknis (TC-75): unduhan berkas CSV ke direktori yang dapat dibaca skrip (nama berkas dan jumlah baris data dibaca); isi kolom From dan Client berkas dibaca oleh skrip.
- General Settings Pre-setup #1 tidak diubah. State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD` dan `AC_DA_TC_P1_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-71: Visibilitas READ Principal

1. Amati tabel List sebagai Principal PT ABC (halaman dibuka hook `beforeEach`)
2. Verifikasi halaman 1 memuat 10 baris
3. Klik nomor halaman 3
4. Verifikasi halaman 3 memuat 10 baris
5. Verifikasi baris `HALC-20260901-00001` pada halaman 3 berpengirim `PT Global Distribusi` (kolom From)
6. Verifikasi baris `HALC-20260901-00003` pada halaman 3 berpengirim `CV Mitra Solusi` (kolom From)
7. Verifikasi baris `HALC-20260902-00003` pada halaman 3 berpengirim `PT ABC` (kolom From)
8. Verifikasi baris `HALC-20260903-00004` pada halaman 3 berpengirim `PT Nusa Distribusi` (kolom From)
9. Verifikasi tabel memuat seluruh transaksi platform: 30 baris pada tiga halaman (10, 10, 10)
10. Ketik Search `Nusa`, tekan Enter
11. Verifikasi tabel menampilkan baris pengirim PT Nusa Distribusi (pengirim di luar jaringan PT Global Distribusi tampil bagi Principal)
12. Klik `(←)` pada kotak Search

### Ganti akun ke Total Control Distributor

13. Logout dari akun Total Control Principal
14. Login sebagai Total Control Distributor (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
15. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-72: Visibilitas READ Distributor

16. Amati tabel List sebagai Total Control Distributor
17. Verifikasi halaman 1 memuat 10 baris
18. Klik nomor halaman 2
19. Verifikasi halaman 2 memuat 10 baris
20. Klik nomor halaman 3
21. Verifikasi halaman 3 memuat 2 baris
22. Verifikasi tabel memuat 22 baris pada tiga halaman (10, 10, 2): 16 baris yang dikirim PT Global Distribusi dan 6 baris yang ditujukan ke Client dalam jaringannya
23. Klik nomor halaman 1
24. Ketik Search `Nusa`, tekan Enter
25. Verifikasi tabel menampilkan "No results found": transaksi PT Nusa Distribusi tidak terlihat
26. Ganti isi kotak search dengan `Manufaktur`, tekan Enter
27. Verifikasi tabel menampilkan "No results found": transaksi PT ABC ke PT Manufaktur Unggul tidak terlihat
28. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
29. Verifikasi tabel menampilkan sedikitnya satu baris (pembanding bahwa Search berfungsi pada scope ini)
30. Klik `(←)` pada kotak Search

### TC-AC-ACHA-73: Visibilitas READ Distributor transitif ke Client Partner

31. Ketik Search `Retail`, tekan Enter
32. Verifikasi enam baris Client `PT Retail Makmur` yang dikirim CV Mitra Solusi (Partner di bawah PT Global Distribusi) tampil
33. Verifikasi baris `HALC-20260904-00003` ada di antara hasil (visibilitas transitif Client yang dipegang Partner)
34. Klik `(←)` pada kotak Search

### TC-AC-ACHA-75: Isi hasil Download mengikuti scope READ

35. Klik ikon Download dan pilih `Download as CSV`
36. Tunggu berkas terunduh
37. Baca berkas CSV yang terunduh
38. Verifikasi berkas memuat 22 baris data, sama dengan baris dalam scope READ Distributor pada List (16 baris yang dikirim PT Global Distribusi dan 6 baris Client dalam jaringannya)
39. Verifikasi tidak ada baris pengirim PT Nusa Distribusi atau PT ABC pada kolom From berkas (di luar scope READ)

### Ganti akun ke Total Control Partner CV Mitra Solusi

40. Logout dari akun Total Control Distributor
41. Login sebagai Total Control Partner CV Mitra Solusi (`totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P1_PASSWORD`)
42. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-74: Visibilitas READ Partner

43. Amati tabel List sebagai Total Control Partner CV Mitra Solusi
44. Verifikasi tabel memuat 6 baris (seluruhnya dikirim CV Mitra Solusi atau ditujukan ke Client terafiliasi langsung PT Retail Makmur)
45. Ketik Search `Sejahtera`, tekan Enter
46. Verifikasi tabel menampilkan "No results found": transaksi PT Global Distribusi tidak terlihat oleh Partner
47. Klik `(←)` pada kotak Search

## Notes

- Ukuran spec (di atas 35 langkah): lima TC scope baca memakai satu dataset Pre-setup dan satu urutan ganti akun; tiap Expected menjadi `Verifikasi` sendiri (S-01) dan memisahkannya menambah ganti akun tanpa nilai uji.
- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec scope baca List per tipe entitas; tanpa aksi tulis. Pengecualian S-12 nama literal: seed Pre-setup #48 (lihat spec 001 Notes).
- Urutan TC di spec: TC-71, TC-72, TC-73, TC-75, TC-74 (penyimpangan dari urutan nomor, S-05): TC-75 memakai akun Distributor yang sama dengan TC-72 dan TC-73 sehingga ganti akun minimal.
- Anchor absence (bagian 8b butir 2): asersi "No results found" pada Search hasil kosong adalah anchor positif yang sah untuk absence hasil Search; asersi "tidak ada baris pengirim PT Nusa Distribusi atau PT ABC" pada berkas TC-75 didahului `Verifikasi` jumlah baris data berkas 22 sebagai pembanding.
- Langkah penghubung (S-03): langkah ganti akun (subjudul "Ganti akun ..."), klik `(←)` yang mereset Search, langkah Search `Sejahtera` pada TC-72 (pembanding bahwa Search berfungsi pada scope Distributor; asersi tambahan atas TC dengan alasan anchor bagian 8b butir 2), langkah Search `Nusa` pada TC-71 (pembanding bahwa pengirim PT Nusa Distribusi tampil bagi Principal sebagai kontras terhadap TC-72 b), tunggu berkas terunduh, dan baca berkas.
- Langkah penghubung halaman (S-14): langkah 17 sampai 23 menelusuri halaman 1, 2, dan 3 sebelum asersi total 22 baris pada tiga halaman (10, 10, 2), lalu klik nomor halaman 1 supaya Search berikutnya mulai dari halaman pertama.
- Pembagian TC lintas spec: Search, Filter, Sort, Pagination umum di spec 036 sampai 041; Download fungsional di spec 043 dan isi berkas di spec 044; scope penerima WRITE di spec 013.
- Temuan untuk QA:
  - TC-72 Expected a dan TC-73 Expected (22 baris, 16 dikirim PT Global Distribusi dan 6 ke Client dalam jaringannya; enam baris PT Retail Makmur) cocok dengan Rincian Seed List Pre-setup #48.
  - TC-71 Expected menyebut empat pengirim yang diamati lewat Allocation ID pada halaman 3 (Langkah Uji 3); spec mengasersi keempat baris itu pada kolom From (satu `Verifikasi` per pengirim). Pembanding Search `Nusa` ditambahkan agar scope Principal teramati terhadap TC-72 b (asersi tambahan, S-03).
  - TC-75 Expected b ("tidak ada baris pengirim PT Nusa Distribusi atau PT ABC") adalah asersi isi sel berkas (kelas f, bagian 3 prinsip 13f); TC-75 ditempatkan di spec ini bersama jumlah baris. TC-75 dapat dipindahkan ke spec 044 bila kelas f harus murni.
  - TC-75 tidak menyebut nama berkas; tidak diasersi.
  - Post Condition TC-71 sampai TC-75 bernilai `-`.
