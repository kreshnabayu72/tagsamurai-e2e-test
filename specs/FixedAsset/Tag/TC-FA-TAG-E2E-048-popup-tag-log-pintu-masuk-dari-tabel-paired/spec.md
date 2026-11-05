---
id: TC-FA-TAG-E2E-048-popup-tag-log-pintu-masuk-dari-tabel-paired
title: "Popup TAG Log: Pintu Masuk dari Klik TAG Code di Popup Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-212
  - TC-FA-TAG-213
  - TC-FA-TAG-214
  - TC-FA-TAG-215
  - TC-FA-TAG-216
  - TC-FA-TAG-217
  - TC-FA-TAG-218
coverage:
  web: automated
---

# Popup TAG Log: Pintu Masuk dari Klik TAG Code di Popup Detail

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Kode | Email (Pre-setup TC) | Env password | Blok |
|---|---|---|---|---|
| Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | TC-FA-TAG-212 sampai TC-FA-TAG-215 dan TC-FA-TAG-218 |
| Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` | TC-FA-TAG-216 |
| Manage asset & TAG (Read) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` | TC-FA-TAG-217 |

- Nama env password usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`. Login Total Control di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk ketiga akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Aset acuan grup Excavator 20 Ton / Plant B: AST-0011 (Tag RF-00101) dan AST-0044 (dua Tag: QR-00232 dan RF-00132).
- Kemampuan teknis (disediakan tim FE/BE): seed idempotent aset dan Tag (RF-00101, QR-00232, RF-00132) lewat fixture backend (lihat `suite.md`); navigasi keyboard (Tab dan Enter).
- Pemulihan di hook `after`: kembalikan data Pre-setup tab Paired ke keadaan awal bila seeding mengubahnya. Spec ini tidak mengubah data bisnis.
- State global: tidak ada. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### Blok Total Control

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B

TC-FA-TAG-212:

2. Klik link TAG Code `RF-00101` pada baris AST-0011
3. Verifikasi Popup TAG Log (Global, read-only) terbuka di atas Popup Detail untuk Tag RF-00101
4. Verifikasi popup hanya memiliki ikon close
5. Tutup Popup TAG Log

TC-FA-TAG-213:

6. Klik `QR-00232` pada baris AST-0044
7. Verifikasi Popup TAG Log terbuka untuk QR-00232
8. Tutup Popup TAG Log
9. Klik `RF-00132` pada baris AST-0044
10. Verifikasi Popup TAG Log terbuka untuk RF-00132
11. Tutup Popup TAG Log

TC-FA-TAG-214:

12. Klik `RF-00101`
13. Klik ikon close Popup TAG Log
14. Verifikasi Popup TAG Log tertutup
15. Verifikasi Popup Detail `Assets` tetap terbuka dengan tabel yang sama

TC-FA-TAG-215:

16. Klik `RF-00101`
17. Klik area gelap di luar popup
18. Verifikasi Popup TAG Log tetap terbuka
19. Klik ikon close Popup TAG Log

TC-FA-TAG-218:

20. Fokuskan link `RF-00101` dengan Tab
21. Tekan Enter
22. Verifikasi Popup TAG Log terbuka
23. Verifikasi Popup TAG Log menerima fokus (focus trap)
24. Klik ikon close Popup TAG Log, lalu tutup Popup Detail

### Blok Read Only

25. Ganti akun: Logout dari akun Total Control, login sebagai Read Only, lalu buka Fixed Asset > TAG tab Paired
26. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
27. Klik `RF-00101`
28. Verifikasi Popup TAG Log terbuka (TC-FA-TAG-216)
29. Tutup Popup TAG Log, lalu tutup Popup Detail

### Blok Manage asset & TAG (Read)

30. Ganti akun: Logout dari akun Read Only, login sebagai Manage asset & TAG (Read), lalu buka Fixed Asset > TAG tab Paired
31. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
32. Klik `RF-00101`
33. Verifikasi Popup TAG Log terbuka (TC-FA-TAG-217)

## Notes

- Mode: FE+BE. Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a); subjudul memetakan langkah ke id TC granular.
- Perubahan urutan (S-05): urutan TC sumber 212, 213, 214, 215, 216, 217, 218 menjadi 212, 213, 214, 215, 218, 216, 217. Alasan: TC Total Control (212 sampai 215 dan 218) dikumpulkan sebelum ganti akun ke Read Only dan Manage asset & TAG (Read) supaya ganti akun terjadi dua kali.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5, 8, 11, 19, 24, dan 29 (menutup Popup TAG Log dan Popup Detail), 25 dan 30 (ganti akun), 1, 26, dan 31 (membuka Popup Detail).
- Langkah 28 dan 33: id TC ditulis di dalam langkah karena blok role tidak memakai subjudul per TC.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-212 Expected a menyebut Popup TAG Log "Global, read-only"; isi popup (kolom dan entri) tidak disebut di Expected TC mana pun pada spec ini, sehingga spec hanya mengasersi popup terbuka untuk Tag yang diklik dan hanya punya ikon close.
  - TC-FA-TAG-214 Expected ("tabel yang sama") tidak menyebut isi tabel yang dibandingkan; spec mengasersi Popup Detail tetap terbuka.
  - TC-FA-TAG-218 mengharapkan fokus pada popup (focus trap) tanpa menyebut elemen yang menerima fokus; spec mengasersi popup menerima fokus.
  - AST-0044 punya dua Tag (QR-00232 dan RF-00132) menurut TC-FA-TAG-213, sedangkan Data Uji TC-FA-TAG-190 menyebut AST-0044 hanya bertag QR-00232 (lihat spec 044).
