---
id: TC-AC-ACTS-E2E-107-lintas-modul-delete-tag-jalur-a-dan-b-dan-auto-resolve-activate
title: "Lintas Modul: Delete TAG Jalur A dan B, Activate TAG Cocok Unit Available Auto-Resolve, dan Activate TAG Cocok Unit In Use Membuat Activation Collision"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-677
  - TC-AC-ACTS-678
  - TC-AC-ACTS-679
  - TC-AC-ACTS-680
coverage:
  web: automated
---

# Lintas Modul: Delete TAG Jalur A dan B, Activate TAG Cocok Unit Available Auto-Resolve, dan Activate TAG Cocok Unit In Use Membuat Activation Collision

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: TAG > Stock (Stock List, dibuka hook `beforeEach` suite).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12) dengan unit milik spec ini, disiapkan seeding fixture BE (disediakan tim FE/BE): unit In Use hasil aktivasi Jalur A (TC-AC-ACTS-677), unit In Use hasil BYO Jalur B dengan SKU (TC-AC-ACTS-678), unit Available dan unit Damaged/Missing (TC-AC-ACTS-679), dan unit In Use milik Client lain (TC-AC-ACTS-680). Client memiliki akses Global Settings > TAG; Delete TAG dan Activate TAG dipicu lewat sesi API aktor (akun Client tidak ada di Pre-setup TC; disediakan tim FE/BE). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca In Use dan Total Registered SKU serta jumlah Subject Tab Active sebagai baseline (S-12). Subject Activation Collision yang dibuat TC-AC-ACTS-680 dan state unit dipulihkan lewat fixture BE di hook `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-677: Delete TAG Jalur A mengembalikan unit ke Available

1. Catat In Use SKU `RFID-ASSET-CORE-R5` di TAG > Stock
2. Client menghapus tag unit Jalur A di Global Settings hingga tersimpan (sesi API aktor)
3. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
4. Muat ulang Tab In Use setiap 5 detik sampai event diproses (batas tunggu 2 menit)
5. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
6. Verifikasi unit kembali Available di Tab Available
7. Buka Tab In Use
8. Verifikasi Tab In Use memuat sedikitnya satu baris unit lain (anchor)
9. Verifikasi unit hilang dari Tab In Use
10. Buka TAG > Stock
11. Verifikasi In Use berkurang 1 terhadap baseline

### TC-AC-ACTS-678: Delete TAG Jalur B menghapus unit yang dibuat saat aktivasi

12. Catat In Use dan Total Registered SKU `RFID-ASSET-CORE-R5` di TAG > Stock
13. Client menghapus tag unit Jalur B di Global Settings hingga tersimpan (sesi API aktor)
14. Muat ulang TAG > Stock setiap 5 detik sampai event diproses (batas tunggu 2 menit)
15. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
16. Verifikasi Tab In Use memuat sedikitnya satu baris unit lain (anchor)
17. Verifikasi unit dihapus (unit Jalur B tidak ada di Detail SKU > Tab In Use)
18. Verifikasi In Use SKU berkurang 1 terhadap baseline
19. Verifikasi Total Registered SKU berkurang 1 terhadap baseline

### TC-AC-ACTS-679: Activate TAG yang match unit Available atau Damaged/Missing auto-resolve tanpa approval

20. Catat baseline jumlah Subject di Approvals > TAG Stock > Tab Active
21. Client mengaktivasi tag yang match unit Available hingga tersimpan (sesi API aktor)
22. Client mengaktivasi tag yang match unit Damaged/Missing hingga tersimpan (sesi API aktor)
23. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
24. Verifikasi kedua unit langsung In Use
25. Buka Approvals > TAG Stock > Tab Active
26. Verifikasi tidak ada Subject baru di Approvals (jumlah Subject sama dengan baseline)

### TC-AC-ACTS-680: Activate TAG yang match unit In Use membuat Subject Activation Collision

27. Client mengaktivasi tag dengan identifier unit In Use milik Client lain hingga tersimpan (sesi API aktor)
28. Buka Approvals > TAG Stock > Tab Active
29. Verifikasi Subject Type Activation Collision muncul di Tab Active dengan unit Waiting for Approval

## Notes

- Mode: FE+BE. Pemicu Client lewat sesi API aktor bukan konteks kedua (P-2 tidak dipakai; keputusan 2026-10-30).
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), membuka layar baca, dan memuat ulang tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit). Pelaku Client ditulis "hingga tersimpan" (R-20).
- Absence unit pada TC-AC-ACTS-677 dan TC-AC-ACTS-678 didahului anchor positif (baris unit lain di Tab In Use; 8b butir 2). Absence Subject pada TC-AC-ACTS-679 memakai baseline jumlah Subject (asersi jumlah, bukan kelas g) dan didahului anchor positif (kedua unit In Use tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-677 sampai TC-AC-ACTS-680 menyebut "Client" tanpa akun dan mekanisme Delete TAG dan Activate TAG; disediakan tim FE/BE.
  - TC-AC-ACTS-678 menyebut "Unit dihapus" tanpa cara mengamati; spec memeriksa Tab In Use dan metrik.
