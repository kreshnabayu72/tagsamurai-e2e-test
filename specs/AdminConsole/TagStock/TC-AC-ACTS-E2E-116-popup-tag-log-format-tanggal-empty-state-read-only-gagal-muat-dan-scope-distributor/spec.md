---
id: TC-AC-ACTS-E2E-116-popup-tag-log-format-tanggal-empty-state-read-only-gagal-muat-dan-scope-distributor
title: "Popup TAG Log: Format Tanggal Mengikuti General Settings, Unit Tanpa Entri (S-29), Read-Only Tanpa Tombol Close, Gagal Dimuat, dan Distributor Hanya Unit Batch Miliknya"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-956
  - TC-AC-ACTS-957
  - TC-AC-ACTS-958
  - TC-AC-ACTS-959
  - TC-AC-ACTS-982
coverage:
  web: automated
---

# Popup TAG Log: Format Tanggal Mengikuti General Settings, Unit Tanpa Entri (S-29), Read-Only Tanpa Tombol Close, Gagal Dimuat, dan Distributor Hanya Unit Batch Miliknya

## Prerequisites

- Mode: FE+BE. Intercept respons TAG Log dengan 5xx lewat `Spectra.intercept()` di atas backend nyata (TC-AC-ACTS-959); request langsung ke server pada TC-AC-ACTS-982 (klien HTTP, kelas a, K-1).
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: Detail SKU `RFID-ASSET-CORE-R5` > Tab Available (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- State global General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta diatur oleh Principal pengubah General Settings lewat sesi API aktor sebelum TC-AC-ACTS-956 (akun pengubah tidak ada di Pre-setup TC; disediakan tim FE/BE). Nilai awal dicatat dan dipulihkan di hook `after` (R-08).
- Data milik spec disiapkan seeding fixture BE (disediakan tim FE/BE): unit dengan sedikitnya satu entri TAG Log, unit tanpa entri (data warisan) pada SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12), serta unit Principal dan unit Distributor lain pada SKU yang sama untuk TC-AC-ACTS-982. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: klien HTTP untuk request TAG Log langsung (asersi hanya status respons, 8b butir 1) dan sesi API aktor Distributor.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-957: Unit tanpa entri menampilkan header dan empty state S-29

1. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
2. Klik (⋯) > `TAG Log` pada unit tanpa entri
3. Verifikasi header tampil lengkap
4. Verifikasi empty state `No log yet` dan `Events for this TAG will appear here.` tampil di bawah header
5. Tutup popup lewat (X)

### TC-AC-ACTS-958: Popup TAG Log read-only, tutup dengan (X) atau Esc, tanpa tombol Close dan tanpa aksi ubah atau hapus

6. Klik (⋯) > `TAG Log` pada unit berentri
7. Klik pada satu entri, lalu hover satu entri
8. Verifikasi popup terbuka dengan sedikitnya satu entri tampil
9. Verifikasi tidak ada tombol `[Close]`
10. Verifikasi tidak ada aksi ubah atau hapus entri
11. Klik (X)
12. Verifikasi popup tertutup oleh (X)
13. Klik (⋯) > `TAG Log` pada unit berentri lagi, tekan `Esc`
14. Verifikasi popup tertutup oleh `Esc`

### TC-AC-ACTS-959: Gagal memuat Popup TAG Log menampilkan error bukan empty state

15. Intercept request TAG Log dengan 5xx
16. Klik (⋯) > `TAG Log` pada unit berentri
17. Verifikasi body popup menampilkan `Unable to load this data.` dan `[Try Again]`
18. Verifikasi body popup bukan empty state
19. Verifikasi header popup tampil
20. Verifikasi (X) tampil
21. Lepas intercept request TAG Log
22. Klik (X)

### TC-AC-ACTS-956: Tanggal dan waktu entri TAG Log mengikuti General Settings

23. Atur General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, dan Timezone Asia/Jakarta hingga tersimpan (sesi API aktor)
24. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) > `TAG Log` pada unit berentri
25. Verifikasi Date & Time tiap entri tampil `dd/MM/yy HH:mm` zona Asia/Jakarta
26. Tutup popup lewat (X)

### TC-AC-ACTS-982: Distributor hanya dapat membuka TAG Log unit batch registrasi miliknya

27. Ganti akun: klik Logout
28. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
29. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
30. Verifikasi tab memuat sedikitnya satu unit milik sendiri (baris pembanding)
31. Verifikasi unit di luar scope (unit Principal) tidak tampil di tab
32. Klik (⋯) > `TAG Log` pada unit milik sendiri
33. Verifikasi TAG Log unit milik sendiri terbuka normal
34. Tutup popup lewat (X)
35. Panggil endpoint TAG Log langsung atas unit Principal (klien HTTP)
36. Verifikasi request ditolak server

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (36 langkah); alasan: semua blok satu permukaan (Popup TAG Log) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- K-1: TC-AC-ACTS-982 memuat request langsung ke server (kelas a) dengan Expected respons API; tetap masuk spec FE+BE dan klausa request langsung hanya mengasersi status respons (8b butir 1). P-5 butir (b): TC-AC-ACTS-959 adalah satu kegagalan 5xx objek-uji ringan (intercept di atas backend nyata) pada permukaan yang sama (Popup TAG Log).
- Urutan TC: TC-AC-ACTS-956 (mengubah state global General Settings) sesudah TC-AC-ACTS-957 sampai TC-AC-ACTS-959 supaya state global dipulihkan sedikit mungkin; TC-AC-ACTS-982 terakhir karena ganti akun (S-10).
- Langkah penghubung tanpa Verifikasi (S-03): menutup popup lewat (X) sebelum langkah berikutnya (S-09), mengatur General Settings lewat sesi API aktor ("hingga tersimpan", R-20), langkah ganti akun, dan melepas intercept.
- Absence tombol `[Close]` dan aksi ubah/hapus entri (TC-AC-ACTS-958) didahului anchor positif (popup terbuka dengan entri tampil; 8b butir 2). Absence unit di luar scope (TC-AC-ACTS-982) didahului pembacaan tab yang sama dengan unit milik sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-956 menyebut "General Settings: Date Format `dd/MM/yy`" tanpa akun pengubah.
  - TC-AC-ACTS-982 menyebut ACC "Distributor Toggle ON (Manage TAG stock, Local Registration aktif)" tanpa id unit; disediakan seeding.
