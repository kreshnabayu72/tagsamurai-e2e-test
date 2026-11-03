---
id: TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal
title: "Scope Data READ dan WRITE: Distributor, Partner, dan Principal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-86
  - TC-AC-LA-87
  - TC-AC-LA-97
  - TC-AC-LA-88
  - TC-AC-LA-89
coverage:
  web: automated
---

# Scope Data READ dan WRITE: Distributor, Partner, dan Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update (PT Maju Bersama) (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Partner satu kantong (Pre-setup #15) `partnerFullLic_automated_{namaCompany}@qwertysystem.net` (`Rian Tarigan`), password `Spectra.env.AC_LA_PARTNER_FULL_PASSWORD`; Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Hasil yang diuji |
|---|---|---|
| `dewiFullLic` (`Dewi Anggraini`) | Distributor Create+Read+Update | READ: baris `PT Sejahtera` dan `PT Abadi Jaya` tampil; WRITE: dropdown Client memuat `PT Sejahtera` dan tidak memuat `PT Abadi Jaya`; Changelog dan Download mengikuti scope READ |
| `partnerFullLic` (`Rian Tarigan`) | Partner satu kantong | baris `PT Abadi Jaya` tampil, `PT Sejahtera` tidak tampil; dropdown Client hanya `PT Abadi Jaya` |
| `totalControlLic` (`Hendra Wijaya`) | Total Control Principal | baris dan opsi Client dalam irisan scope entitas dan scope group Manage allocation tampil, di luar scope tidak tampil |

- Data Pre-setup yang dibaca: #19 PT Sejahtera (binaan langsung Distributor PT Maju Bersama), #20 Klinik Medika Jaya, #25 PT Abadi Jaya (dipegang Partner CV Karya Mandiri di bawah Distributor PT Maju Bersama), dan #54 (30 alokasi lintas status). Seed hanya dibaca. N baris tab Current dalam scope READ Distributor `dewiFullLic` diturunkan dari seeding dan dicatat di `Fixture.license-allocation-license` (kunci countScopeReadDistributor).
- Kemampuan teknis (disediakan tim FE/BE): baca nama berkas dan jumlah baris data berkas unduhan CSV; isi sel berkas tidak diasersi (kelas f). Client di luar scope group akun `totalControlLic` untuk TC-AC-LA-89 tidak tertulis di Pre-setup TC dan disediakan tim FE (kunci clientLuarScopeGroup di fixture; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-86: Distributor melihat Client binaan sendiri dan Client yang dipegang Partner

1. Ketik Search `PT Sejahtera`, tekan Enter
2. Verifikasi baris alokasi `PT Sejahtera` tampil
3. Ganti isi kotak search dengan `PT Abadi Jaya`, tekan Enter
4. Verifikasi baris alokasi `PT Abadi Jaya` (dipegang Partner `CV Karya Mandiri`) tampil
5. Klik `(←)` pada kotak Search

### TC-AC-LA-87: Distributor hanya memilih Client binaan langsung pada dropdown Client

6. Klik `[+ Allocation]` dan buka dropdown Client
7. Cari `PT Sejahtera` pada dropdown Client
8. Verifikasi `PT Sejahtera` muncul pada opsi Client
9. Cari `PT Abadi Jaya` pada dropdown Client
10. Verifikasi `PT Abadi Jaya` tidak muncul pada opsi Client
11. Tutup form dengan `[✕]`

### TC-AC-LA-97: Changelog dan hasil Download mengikuti row scope READ

12. Klik ikon Changelog untuk membuka modal Changelog
13. Ketik Search `PT Sejahtera` pada modal Changelog, tekan Enter
14. Verifikasi Changelog memuat entri alokasi Client binaan `PT Sejahtera`
15. Ganti isi kotak search modal Changelog dengan `PT Abadi Jaya`, tekan Enter
16. Verifikasi Changelog memuat entri alokasi Client Partner `PT Abadi Jaya` dalam jaringan
17. Tutup modal Changelog dengan `[✕]`
18. Klik Download as CSV pada tab Current
19. Verifikasi jumlah baris data berkas sama dengan N baris tab Current dalam scope READ Distributor

### TC-AC-LA-88: Partner hanya melihat baris Client yang dipegang

20. Ganti akun: Logout lalu login sebagai Partner satu kantong (`partnerFullLic`)
21. Ketik Search `PT Abadi Jaya`, tekan Enter
22. Verifikasi baris `PT Abadi Jaya` tampil
23. Ganti isi kotak search dengan `PT Sejahtera`, tekan Enter
24. Verifikasi empty state `No results found` tampil dan baris `PT Sejahtera` tidak tampil
25. Klik `(←)` pada kotak Search, lalu klik `[+ Allocation]` dan buka dropdown Client
26. Verifikasi dropdown Client hanya memuat `PT Abadi Jaya`
27. Tutup form dengan `[✕]`

### TC-AC-LA-89: Principal melihat dan memilih Client dalam irisan scope

28. Ganti akun: Logout lalu login sebagai Total Control Principal (`totalControlLic`)
29. Ketik Search `PT Sejahtera`, tekan Enter
30. Verifikasi baris Client dalam scope group `PT Sejahtera` tampil
31. Ganti isi kotak search dengan `Klinik Medika Jaya`, tekan Enter
32. Verifikasi baris Client dalam scope group `Klinik Medika Jaya` tampil
33. Ganti isi kotak search dengan nama Client di luar scope group (`Fixture.license-allocation-license`, kunci clientLuarScopeGroup; disediakan tim FE), tekan Enter
34. Verifikasi empty state `No results found` tampil
35. Verifikasi baris Client di luar scope group tidak tampil
36. Klik `(←)` pada kotak Search, lalu klik `[+ Allocation]` dan buka dropdown Client
37. Verifikasi opsi Client memuat `PT Sejahtera` dan `Klinik Medika Jaya`
38. Verifikasi Client di luar scope group tidak muncul pada opsi Client
39. Tutup form dengan `[✕]`, lalu klik ikon Filter dan buka filter Client
40. Verifikasi opsi filter Client memuat `PT Sejahtera` dan `Klinik Medika Jaya`
41. Verifikasi Client di luar scope group tidak muncul pada opsi filter Client

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah `Klik (←)` pada kotak Search, penutupan form dan modal, dan ganti akun eksplisit (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil dan data berbeda per role.
- Spec ini di atas 35 langkah. Alasannya: semua blok satu topik (scope data READ dan WRITE per entitas) dan satu kelas harness (Role Matrix), dan tiap blok akun berdiri sendiri dengan data milik sendiri; kegagalan satu akun tidak membuat blok akun lain kehilangan makna.
- TC-AC-LA-97 (Changelog dan Download) memakai asersi jumlah baris dan nama pada Changelog (kelas f: isi sel berkas tidak diasersi, bagian 3 prinsip 13f 2026-10-30); urutan dalam TC-AC-LA-87 diubah dari TC (cari `PT Abadi Jaya` dulu) menjadi cari `PT Sejahtera` dulu supaya absence `PT Abadi Jaya` punya anchor positif (bagian 8b butir 2).
- Langkah 33 sampai 35 mengasersi bahwa Client di luar scope group tidak tampil pada list (TC-AC-LA-89 Expected a); anchor positifnya adalah baris `PT Sejahtera` dan `Klinik Medika Jaya` pada langkah 30 dan 32 (bagian 8b butir 2). Langkah Search Client di luar scope adalah langkah penghubung (R-16).
- Temuan untuk QA:
  - TC-AC-LA-89 Expected a menyebut `Client di luar scope group tidak tampil` tanpa menyebut Client mana yang di luar scope, sedangkan Pre-setup TC hanya memuat Client dalam scope; spec memakai Client di luar scope yang disediakan tim FE.
  - TC-AC-LA-97 Expected b (`berkas ... tidak memuat Client di luar scope`) adalah asersi isi sel berkas (kelas f); spec hanya mengasersi jumlah baris.
  - TC-AC-LA-87 dan TC-AC-LA-88 tidak menyebut apakah form `[+ Allocation]` dengan dropdown yang dibuka dan dicari dianggap dirty; spec menutup form dengan `[✕]` tanpa dialog Unsaved Changes.
  - TC-AC-LA-97 langkah 1 menyebut `cari entri Client PT Abadi Jaya` pada Changelog tanpa menyebut kolom Changelog yang dicari; spec memakai Search modal Changelog.
