---
id: TC-AC-ACTS-E2E-113-defense-in-depth-request-langsung-tanpa-capability-distributor-dan-toggle-off
title: "Defense-in-Depth: Request Tulis Langsung Tanpa Capability, Partner atau Client, Distributor Approve, Audit, Delete Unit Bukan Miliknya, Toggle OFF, Isolasi Entitas, dan Endpoint QR"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-701
  - TC-AC-ACTS-702
  - TC-AC-ACTS-703
  - TC-AC-ACTS-704
  - TC-AC-ACTS-705
  - TC-AC-ACTS-707
  - TC-AC-ACTS-708
coverage:
  web: automated
---

# Defense-in-Depth: Request Tulis Langsung Tanpa Capability, Partner atau Client, Distributor Approve, Audit, Delete Unit Bukan Miliknya, Toggle OFF, Isolasi Entitas, dan Endpoint QR

## Prerequisites

- Mode: FE+BE. Request langsung ke server lewat klien HTTP (kelas a, K-1).
- Akun aktor: Partner (tanpa akses TAG > Stock) `partner_automated_{namaCompany}@qwertysystem.net` (Pre-setup #17), password dari `Spectra.env.AC_PARTNER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Role Lain tanpa capability `roleLain_automated_{namaCompany}@qwertysystem.net` (Pre-setup #11), password dari `Spectra.env.AC_ROLELAIN_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Distributor Toggle OFF `distributorOff_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10), password dari `Spectra.env.AC_DIST_OFF_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: tidak ada halaman UI yang dibuka oleh langkah spec ini; seluruh langkah adalah request langsung lewat klien HTTP dengan sesi API aktor masing-masing akun (Partner tidak punya akses TAG > Stock).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kemampuan teknis disediakan tim FE/BE: klien HTTP untuk request Add Stock, Audit Submit, Delete, Approve, daftar unit, Event Log, serta Generate QR dan Print/Mark as Printed; sesi API aktor per akun (login API password, token tidak dihitung sebagai sesi web); kemampuan baca status respons dan state data (jumlah unit, status unit, jumlah Subject) lewat fixture BE. Endpoint tidak dikarang di spec; nama dan bentuk request mengikuti kemampuan klien HTTP yang disediakan.
- Data milik spec disiapkan seeding fixture BE (disediakan tim FE/BE): Subject pending (TC-AC-ACTS-702), unit Principal dan unit Distributor lain (TC-AC-ACTS-703, TC-AC-ACTS-704, TC-AC-ACTS-707), dan unit Available milik entitas aktor. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Toggle Local Registration Distributor OFF (TC-AC-ACTS-705) dipakai lewat akun Distributor Toggle OFF (Pre-setup #10) tanpa mengubah toggle; spec ini tidak mengubah state global.
- Env var password akun aktor: `Spectra.env.AC_PARTNER_PASSWORD`, `Spectra.env.AC_ROLELAIN_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`, `Spectra.env.AC_DIST_OFF_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_PARTNER_PASSWORD`, `AC_ROLELAIN_PASSWORD`, `AC_DIST_ON_PASSWORD`, `AC_DIST_OFF_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-701: Permintaan tulis langsung tanpa capability atau dari Partner atau Client ditolak server

1. Catat baseline jumlah unit SKU dan jumlah Subject pending
2. Sebagai Partner (sesi API), kirim request Add Stock, Audit, Delete, dan Approve langsung ke endpoint
3. Verifikasi semua request Partner ditolak server dan tidak diproses
4. Ganti sesi API ke Role Lain tanpa capability (`roleLain_automated_{namaCompany}@qwertysystem.net`)
5. Sebagai Role Lain, kirim request Add Stock, Audit, Delete, dan Approve langsung ke endpoint
6. Verifikasi semua request Role Lain ditolak server dan tidak diproses
7. Verifikasi jumlah unit dan jumlah Subject sama dengan baseline

### TC-AC-ACTS-702: Distributor tidak dapat Approve atau Reject lewat request langsung

8. Ganti sesi API ke Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
9. Kirim request Approve langsung ke endpoint atas Subject pending
10. Verifikasi request ditolak server
11. Verifikasi Subject tetap pending

### TC-AC-ACTS-703: Distributor tidak dapat Audit unit yang bukan miliknya (request langsung)

12. Kirim Audit Submit langsung berisi ID unit Principal atau Distributor lain
13. Verifikasi seluruh permintaan ditolak (bukan di-skip)
14. Verifikasi tidak ada perubahan status unit

### TC-AC-ACTS-704: Distributor tidak dapat Delete unit yang bukan miliknya (request langsung)

15. Kirim Delete langsung untuk unit Principal
16. Verifikasi request ditolak server
17. Verifikasi unit tetap ada

### TC-AC-ACTS-707: Isolasi entitas, Distributor A tidak mendapat data Distributor B lewat endpoint list

18. Panggil endpoint daftar unit dan Event Log langsung sebagai Distributor A
19. Verifikasi respons memuat unit milik Distributor A sendiri (anchor)
20. Verifikasi respons tidak memuat unit atau entri milik Distributor B

### TC-AC-ACTS-705: Toggle Local Registration OFF, request Add Stock langsung ditolak

21. Ganti sesi API ke Distributor Toggle OFF (`distributorOff_automated_{namaCompany}@qwertysystem.net`)
22. Kirim Add Stock langsung ke endpoint
23. Verifikasi request ditolak server karena toggle dicek di endpoint
24. Verifikasi tidak ada unit tersimpan

### TC-AC-ACTS-708: Endpoint tulis QR tidak dikenali di Admin Console

25. Ganti sesi API ke Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`)
26. Panggil endpoint Generate QR atau Print/Mark as Printed
27. Verifikasi resource tidak dikenali (bukan sekadar ditolak)

## Notes

- Mode: FE+BE. K-1: seluruh TC spec ini adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE dan hanya mengasersi status respons dan state data lewat fixture BE (8b butir 1). Perilaku UI untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung tanpa Verifikasi (S-03): langkah ganti sesi API ke akun lain (langkah 4, 8, 21, dan 25; ganti akun punya langkah eksplisit, S-07) dan mencatat baseline (S-12).
- Urutan TC: TC-AC-ACTS-705 sesudah TC-AC-ACTS-707 dan TC-AC-ACTS-708 terakhir supaya penggantian sesi hanya satu kali per akun (S-10).
- Temuan untuk QA:
  - TC-AC-ACTS-701 menyebut "UI menampilkan toast `You don't have permission to do this.` bila dipicu dari UI"; sesuai 8b butir 1 klausa ini tidak disalin dan tidak diasersi di spec request langsung.
  - TC-AC-ACTS-701 menyebut ACC "Partner (dan Role Lain)" sedangkan judul menyebut Partner atau Client; Pre-setup #18 Client tidak dipakai TC ini. Spec menguji Partner dan Role Lain.
  - TC-AC-ACTS-707 menyebut "Distributor A" dan "Distributor B" tanpa akun B; disediakan seeding (unit milik Distributor B).
