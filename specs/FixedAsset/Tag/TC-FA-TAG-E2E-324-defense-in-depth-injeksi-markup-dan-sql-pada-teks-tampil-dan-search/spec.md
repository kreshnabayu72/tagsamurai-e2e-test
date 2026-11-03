---
id: TC-FA-TAG-E2E-324-defense-in-depth-injeksi-markup-dan-sql-pada-teks-tampil-dan-search
title: "Defense-in-Depth: Injeksi Markup dan SQL Ditampilkan sebagai Teks pada Tabel, Changelog, Search, dan TAG Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1259
  - TC-FA-TAG-1260
  - TC-FA-TAG-1261
  - TC-FA-TAG-1307
  - TC-FA-TAG-1308
coverage:
  web: automated
---

# Defense-in-Depth: Injeksi Markup dan SQL Ditampilkan sebagai Teks pada Tabel, Changelog, Search, dan TAG Log

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG dengan Update di group Disposal Center | `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: Total Control (blok 1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 2; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) seed lewat fixture backend untuk data berisi markup: aset di grup 'Excavator 20 Ton' / Plant B dengan Brand `<img src=x onerror=alert(1)>` dan entri Changelog Paired TAG dengan Name `<script>alert(1)</script>`; (2) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned; (3) pengamatan dialog `alert` browser (dipakai untuk memastikan tidak ada eksekusi script). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |
| Brand berisi markup | `<img src=x onerror=alert(1)>` pada aset di grup Plant B | `brandMarkup` |
| Name Changelog berisi script | `<script>alert(1)</script>` | `changelogScript` |
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |

- State yang diubah dan pemulihannya: langkah 20 s.d. 23 mengubah Tag `RF-00071` menjadi Damaged/Missing lewat Receive Manually; hook `after` memulihkan `RF-00071` ke To Be Returned lewat fixture backend, menghapus data markup, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Blok 1: Total Control (TC-FA-TAG-1259, TC-FA-TAG-1260, TC-FA-TAG-1261, TC-FA-TAG-1308)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
2. Verifikasi sel Brand aset tersebut menampilkan teks `<img src=x onerror=alert(1)>` apa adanya sebagai teks
3. Verifikasi tidak ada eksekusi script dan tidak ada dialog alert
4. Tutup Popup Detail dengan ikon close
5. Klik tombol `Changelog` pada Table Tools
6. Verifikasi baris Changelog dengan Name `<script>alert(1)</script>` menampilkan teks apa adanya
7. Verifikasi tidak ada eksekusi script pada Modal Changelog
8. Tutup Modal Changelog
9. Klik ikon Search, ketik Search `' OR 1=1 --`, tekan Enter
10. Verifikasi `No results found` tampil
11. Verifikasi tabel tidak menampilkan seluruh data grup
12. Klik `(←)` pada kotak Search
13. Klik tab `To Be Returned`
14. Klik ikon Search, ketik Search `<script>alert(1)</script>`, tekan Enter
15. Verifikasi tabel menampilkan `No results found`
16. Verifikasi tidak ada script yang dijalankan
17. Klik `(←)` pada kotak Search

### Blok 2: Update di group Disposal Center (TC-FA-TAG-1307)

18. Logout dari akun Total Control, lalu Login sebagai akun Manage asset & TAG dengan Update di group Disposal Center
19. Buka Fixed Asset > TAG > To Be Returned
20. Buka menu aksi baris RF-00071
21. Klik "Receive Manually"
22. Isi Textarea "Note" dengan "<script>alert(1)</script>"
23. Klik tombol [Submit]
24. Tunggu aksi selesai (dialog "Receive Manually" menutup)
25. Buka Global Settings > TAG
26. Ketik Search `RF-00071`, tekan Enter
27. Buka Popup TAG Log untuk RF-00071
28. Verifikasi entri "Marked Damaged/Missing" menampilkan Note sebagai teks literal "<script>alert(1)</script>"
29. Verifikasi tidak ada eksekusi script dan tidak ada dialog alert

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1259 s.d. 1261, 1307, 1308). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec: TC-1259, TC-1260, TC-1261, TC-1308 (akun Total Control, hanya membaca), lalu TC-1307 di akun lain karena Receive Manually mengubah state dan butuh ganti akun.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4, 8, 12, 17 (menutup popup atau modal dan menutup input Search lewat `(←)`), 18 (ganti akun), 24 (menunggu aksi selesai karena langkah berikutnya berpindah surface), 26 (Search untuk menemukan Tag RF-00071 di Global Settings > TAG).
- Asersi "tidak ada eksekusi script" (langkah 3, 7, 16, 29) selalu didahului `Verifikasi` yang menampilkan teks literalnya atau `No results found` pada surface yang sama sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-TAG-1307 meminta akun Update di group Disposal Center membuka Global Settings > TAG; TC tidak menyatakan akun itu punya akses menu tersebut. Spec mengikuti TC.
  - TC-FA-TAG-1259 tidak menyebut aset yang memegang Brand markup selain berada di grup Plant B; spec memakai aset seed milik spec di grup itu.
  - Post Condition TC-FA-TAG-1307 tidak ada; perubahan Tag `RF-00071` menjadi Damaged/Missing dipulihkan hook `after`.
  - Nama dan kode literal Pre-setup (Asset Name, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
