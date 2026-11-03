---
id: TC-AC-DS-E2E-061-edit-validasi-kosong-model-sku-foto-dan-clear-field
title: "Edit SKU: Validasi Model/Type, SKU, Foto Kosong, dan Clear Field Lalu Save"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-209
  - TC-AC-DS-210
  - TC-AC-DS-211
  - TC-AC-DS-212
coverage:
  web: automated
---

# Edit SKU: Validasi Model/Type, SKU, Foto Kosong, dan Clear Field Lalu Save

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke nilai Pre-setup #29 (Device Name `UHF Handheld Reader`, SKU `HHR-ARC-200`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0, 1 foto, Last Modified `28/09/26 14:40`). Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`

### TC-AC-DS-209: Model/Type kosong

2. Hapus seluruh teks Model/Type sampai kosong
3. Klik `[Save]`
4. Verifikasi pesan inline "Model/type must not be empty" tampil
5. Verifikasi popup Edit tetap terbuka
6. Ketik ulang Model/Type `H200`

### TC-AC-DS-210: SKU kosong

7. Hapus seluruh teks SKU sampai kosong
8. Klik `[Save]`
9. Verifikasi pesan inline "SKU must not be empty" tampil
10. Verifikasi popup Edit tetap terbuka
11. Ketik ulang SKU `HHR-ARC-200`

### TC-AC-DS-211: Foto kosong

12. Hapus satu-satunya foto sehingga slot kosong
13. Klik `[Save]`
14. Verifikasi pesan inline pada slot Photo "Photo must not be empty" tampil
15. Verifikasi popup Edit tetap terbuka

### TC-AC-DS-212: Clear Field lalu Save

16. Klik `[Clear Field]`
17. Klik `[Save]`
18. Verifikasi pesan "Device name must not be empty" tampil pada field Device Name
19. Verifikasi pesan "Brand must not be empty" tampil pada field Brand
20. Verifikasi pesan "Model/type must not be empty" tampil pada field Model/Type
21. Verifikasi pesan "SKU must not be empty" tampil pada field SKU
22. Verifikasi pesan "Range type must not be empty" tampil pada field Range Type
23. Verifikasi pesan "Photo must not be empty" tampil pada slot Photo
24. Verifikasi popup Edit tetap terbuka

### Penutupan form dan nilai tersimpan tidak berubah (Expected b TC-209 sampai TC-212)

25. Klik `✕` pada header popup Edit SKU
26. Verifikasi dialog Unsaved Changes tampil
27. Klik `[Leave]`
28. Verifikasi baris `HHR-ARC-200` menampilkan Model/Type `H200` (nilai tersimpan TC-209 tidak berubah)
29. Verifikasi baris `HHR-ARC-200` menampilkan SKU `HHR-ARC-200` (nilai tersimpan TC-210 tidak berubah)
30. Verifikasi thumbnail foto baris `HHR-ARC-200` masih tampil (foto tersimpan TC-211 tidak berubah)
31. Verifikasi baris `HHR-ARC-200` menampilkan Device Name `UHF Handheld Reader` dan Brand `Arcturus` (nilai tersimpan TC-212 tidak berubah)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: Expected "nilai tersimpan tidak berubah" TC-209 sampai TC-212 diasersi sekali setelah popup ditutup (langkah 27 dan sesudahnya), karena nilai tersimpan hanya teramati di baris List sedangkan popup menutupinya.
- Langkah penghubung: langkah 6 dan 11 (mengetik ulang nilai agar pesan error blok berikutnya tidak tercampur, R-12) dan langkah 25 sampai 27 (menutup form dirty: `✕`, dialog Unsaved Changes, `[Leave]`, S-08).
- Temuan untuk QA: Post Condition TC-209 sampai TC-212 kosong. Nilai Range Type baris tidak diasersi karena kolom Range Type Hidden secara default.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
