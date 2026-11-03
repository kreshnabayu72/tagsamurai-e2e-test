---
id: TC-AC-DS-E2E-058-edit-field-terkunci-saat-stok-lebih-dari-nol
title: "Edit SKU: Field SKU, Range Type, dan User TAG Terkunci saat Stok Lebih dari 0 serta Terbuka Kembali saat Stok Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-184
  - TC-AC-DS-185
  - TC-AC-DS-186
  - TC-AC-DS-239
coverage:
  web: automated
---

# Edit SKU: Field SKU, Range Type, dan User TAG Terkunci saat Stok Lebih dari 0 serta Terbuka Kembali saat Stok Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC; SKU hanya dibuka di popup Edit tanpa disimpan sehingga tidak diubah dan Last Modified tidak berubah): SKU inti #29 `HHR-ARC-100` (stok 120, Range Type `Long Range`) dan `TAG-ARC-USR` (stok 500, This is User TAG tercentang); pohon Category #25, Device Name #26, Brand #27, dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `LOCK-HHR-{runId}-058` (Category `UHF Handheld`, Device Name `UHF Handheld Reader`, Brand `Arcturus`, Model/Type `H-LK`, Range Type `Long Range`) dengan stok lebih dari 0 yang di-seed di hook `before`; modul stok (Data Pre-setup #39) mengosongkan seluruh unit pada langkah 24. Spec memakai SKU milik spec ini menggantikan `HHR-ARC-100` pada TC-AC-DS-239 agar stok SKU Pre-setup (120) tidak berubah. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-058`.
- Kemampuan teknis (disediakan tim FE/BE): seeding SKU dengan stok lebih dari 0 dan pengosongan seluruh unit lewat Fixture BE atau Add Stock (Data Pre-setup #39); mekanisme dan endpoint-nya tidak tercantum di TC sehingga tidak disebut di sini.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-184: Edit SKU stok lebih dari 0: field SKU terkunci dengan tooltip

1. Ketik Search `HHR-ARC-100`, tekan Enter
2. Klik ⋯ pada baris `HHR-ARC-100` lalu pilih `Edit`
3. Verifikasi field SKU `HHR-ARC-100` tampil disabled (tetap terlihat) dan tidak dapat diubah
4. Hover field SKU
5. Verifikasi hover menampilkan tooltip "SKU code cannot be changed after stock has been registered."
6. Pindahkan fokus keyboard ke field SKU
7. Verifikasi fokus keyboard menampilkan tooltip "SKU code cannot be changed after stock has been registered."

### TC-AC-DS-185: Edit SKU stok lebih dari 0: field Range Type terkunci dengan tooltip

8. Verifikasi field Range Type `Long Range` tampil disabled dan tidak dapat diubah
9. Hover field Range Type
10. Verifikasi hover menampilkan tooltip "Range type cannot be changed after stock has been registered."
11. Pindahkan fokus keyboard ke field Range Type
12. Verifikasi fokus keyboard menampilkan tooltip "Range type cannot be changed after stock has been registered."
13. Klik ikon close `[✕]` pada popup Edit SKU

### TC-AC-DS-186: Edit SKU stok lebih dari 0: checkbox This is User TAG terkunci dengan tooltip

14. Ganti isi kotak search dengan `TAG-ARC-USR`, tekan Enter
15. Klik ⋯ pada baris `TAG-ARC-USR` lalu pilih `Edit`
16. Verifikasi checkbox `This is User TAG` tampil tercentang dalam keadaan disabled dan tidak dapat diubah
17. Hover checkbox `This is User TAG`
18. Verifikasi hover menampilkan tooltip "User TAG setting cannot be changed after stock has been registered."
19. Pindahkan fokus keyboard ke checkbox `This is User TAG`
20. Verifikasi fokus keyboard menampilkan tooltip "User TAG setting cannot be changed after stock has been registered."
21. Klik ikon close `[✕]` pada popup Edit SKU

### TC-AC-DS-239: Field terkunci kembali dapat diedit setelah seluruh unit dikosongkan dari inventori

22. Ganti isi kotak search dengan `LOCK-HHR-{runId}-058`, tekan Enter
23. Klik ⋯ pada baris `LOCK-HHR-{runId}-058` lalu pilih `Edit`
24. Dengan Fixture BE kosongkan seluruh unit `LOCK-HHR-{runId}-058` sehingga Current Stock menjadi 0
25. Klik ikon close `[✕]` pada popup Edit SKU
26. Klik ⋯ pada baris `LOCK-HHR-{runId}-058` lalu pilih `Edit`
27. Verifikasi field SKU, Device Name, dan Range Type tampil enabled tanpa tooltip kunci
28. Verifikasi popup Edit SKU tidak memuat kontrol un-delete: perubahan stok hanya mengubah status kunci field
29. Klik ikon close `[✕]` pada popup Edit SKU
30. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1, 14, 22, dan 30 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 13, 21, 25, dan 29 menutup popup Edit SKU yang tidak diubah (form bersih, tanpa dialog Unsaved Changes). TC-AC-DS-185 melanjutkan popup TC-AC-DS-184 (SKU `HHR-ARC-100` yang sama, bagian 3).
- Asersi tooltip sementara (bagian 8b butir 5) diletakkan segera sesudah hover atau fokus dan sebelum langkah berikutnya.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-058` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-239 memakai `HHR-ARC-100` Pre-setup dan mengosongkan stoknya; spec memakai SKU milik spec `LOCK-HHR-{runId}-058` supaya stok Pre-setup tidak berubah (S-06). Asersi field terkunci terbuka kembali tetap sama.
  - TC-AC-DS-239 Expected b ("tidak ada mekanisme un-delete") tidak punya cara pengamatan yang jelas di TC; spec mengasersi tidak adanya kontrol un-delete pada popup Edit dengan anchor field enabled.
