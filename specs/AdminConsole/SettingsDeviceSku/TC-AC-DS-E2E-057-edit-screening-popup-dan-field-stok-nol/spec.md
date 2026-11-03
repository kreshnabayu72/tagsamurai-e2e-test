---
id: TC-AC-DS-E2E-057-edit-screening-popup-dan-field-stok-nol
title: "Edit SKU: Screening Popup, Category Read-only, Stok 0 Semua Field Editable, dan Device Name Read-only Stok Berisi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-181
  - TC-AC-DS-182
  - TC-AC-DS-183
  - TC-AC-DS-187
  - TC-AC-DS-188
coverage:
  web: automated
---

# Edit SKU: Screening Popup, Category Read-only, Stok 0 Semua Field Editable, dan Device Name Read-only Stok Berisi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC; SKU hanya dibuka di popup Edit tanpa disimpan sehingga tidak diubah dan Last Modified tidak berubah): SKU inti #29 `HHR-ARC-200` (UHF Handheld, Arcturus, `H200`, stok 0, Range Type `Short Range`), `HHR-ARC-100` (stok 120, Device Name `UHF Handheld Reader`), dan `SFR-VEL-4P` (stok 36, Port `8080`); pohon Category #25, Device Name #26, Brand #27, dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak menyimpan perubahan sehingga tidak membuat SKU dan tidak ada cleanup.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-181: Screening Popup Edit SKU: judul, field pre-filled, Category read-only, dan footer tanpa checkbox Stay

1. Ketik Search `HHR-ARC-200`, tekan Enter
2. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
3. Verifikasi Header: judul popup `Edit SKU`
4. Verifikasi Header: ikon close `[✕]` di sudut kanan atas
5. Verifikasi Body: Category terisi `UHF Handheld` dalam keadaan read-only (tidak dapat dibuka)
6. Verifikasi Body: Device Name `UHF Handheld Reader`, Brand `Arcturus`, Model/Type `H200`, dan SKU `HHR-ARC-200` terisi
7. Verifikasi Body: Device Name, Brand, Model/Type, dan SKU dapat diedit karena Current Stock 0
8. Verifikasi Body: Photo menampilkan foto SKU yang tersimpan
9. Verifikasi Body: Range Type `Short Range` terisi karena ancestry Handheld Reader
10. Verifikasi Body: Port dan This is User TAG tidak tampil
11. Verifikasi Body: helper text di bawah field SKU "Letters, numbers, hyphens, and dots only (e.g. SKU-RFID-V2)"
12. Verifikasi Footer: tombol `[Clear Field]` dan `[Save]` rata kanan
13. Verifikasi Footer: tidak ada checkbox `Stay on this form after submitting` dan tidak ada tombol `[Cancel]`

### TC-AC-DS-182: Field Category pada Popup Edit SKU bersifat read-only dan tidak dapat diubah

14. Klik field Category
15. Tekan Enter dan Space saat fokus pada field Category
16. Verifikasi field Category tetap menampilkan `UHF Handheld`
17. Verifikasi picker Category tidak terbuka
18. Verifikasi tidak ada pohon Category yang muncul
19. Verifikasi nilai Category tidak berubah

### TC-AC-DS-183: Edit SKU stok 0: semua field selain Category dapat diedit

20. Periksa status field SKU, Device Name, Range Type, Brand, Model/Type, dan Photo
21. Verifikasi field SKU, Device Name, Range Type, Brand, Model/Type, dan Photo berstatus enabled tanpa tooltip kunci
22. Verifikasi field Category berstatus read-only
23. Verifikasi kode SKU dapat diubah pada SKU berstok 0
24. Klik ikon close `[✕]` pada popup Edit SKU

### TC-AC-DS-187: Edit SKU stok lebih dari 0: Device Name read-only dengan inline info

25. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
26. Klik ⋯ pada baris `HHR-ARC-100` lalu pilih `Edit`
27. Verifikasi field Device Name `UHF Handheld Reader` tampil read-only
28. Verifikasi inline info di bawah field menampilkan "Device name cannot be changed while this SKU has stock."
29. Klik ikon close `[✕]` pada popup Edit SKU

### TC-AC-DS-188: Edit SKU stok lebih dari 0: Brand, Model/Type, Photo, dan Port tetap dapat diedit

30. Ganti isi kotak search dengan `SFR-VEL-4P`, tekan Enter
31. Klik ⋯ pada baris `SFR-VEL-4P` lalu pilih `Edit`
32. Verifikasi field Brand, Model/Type, Photo, dan Port `8080` berstatus enabled pada SKU berstok 36
33. Verifikasi field SKU dan Device Name terkunci
34. Klik ikon close `[✕]` pada popup Edit SKU
35. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1, 25, 30, dan 35 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 24, 29, dan 34 menutup popup Edit SKU yang tidak diubah (form bersih, tanpa dialog Unsaved Changes). Pemakaian ulang popup (bagian 3): TC-AC-DS-182 dan TC-AC-DS-183 melanjutkan popup TC-AC-DS-181.
- Urutan TC diubah: TC-AC-DS-187 dan TC-AC-DS-188 (SKU berstok lebih dari 0) dijalankan sesudah blok SKU berstok 0 agar popup yang sama dipakai ulang.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-057` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-181 Expected b.ii dan TC-AC-DS-183 Expected a memakai kata "dapat diedit"/"enabled" tanpa mengetik; spec mengasersi status kontrol, bukan hasil pengetikan.
