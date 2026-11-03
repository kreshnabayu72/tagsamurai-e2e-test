---
id: TC-FA-TAG-E2E-146-report-tag-submit-berhasil-per-report-type-dan-dampaknya-bagian-2
title: "Report TAG: Dampak Laporan pada Status Aset, Registri Global, dan Kartu Reported (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-613
  - TC-FA-TAG-614
  - TC-FA-TAG-615
  - TC-FA-TAG-616
coverage:
  web: automated
---

# Report TAG: Dampak Laporan pada Status Aset, Registri Global, dan Kartu Reported (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Langkah ganti akun ditulis eksplisit (Logout lalu Login). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): pembacaan nilai kartu dan kolom "Reported" sebelum aksi lewat fixture backend untuk baseline N (dicatat di hook `before`, sebelum langkah pertama), dan pembacaan status Tag di registri Global lewat UI Global Settings > TAG.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' | AST-0020, Group Plant B, status Assigned; Tag tunggal RFID `RF-00130` Paired | `aset20` |
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |
| Baseline N | nilai kartu "Reported" dan kolom "Reported" baris grup Excavator 20 Ton · Plant B sebelum aksi, dicatat di hook `before` (kemampuan baca disediakan tim FE/BE) | `baselineReportedN` |

- State yang diubah dan pemulihannya: laporan terbuka yang dibuat spec ini pada `RF-00130` dan `QR-00232` dibatalkan dan data dipulihkan lewat fixture backend di hook `after`; spec selesai di akun Total Control sehingga sesi sudah di akun default suite.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Satu Report TAG Damaged pada AST-0020 sebagai dasar TC-FA-TAG-614 dan TC-FA-TAG-616

2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Klik [Submit]
6. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)
7. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], login dengan akun Total Control [TC], lalu buka Fixed Asset > TAG tab Paired

### Kartu Reported dan kolom Reported grup (TC-FA-TAG-616)

8. Verifikasi kartu "Reported" bernilai N + 1
9. Verifikasi kolom "Reported" baris grup Excavator 20 Ton · Plant B bernilai N + 1
10. Klik kartu "Reported"
11. Verifikasi kartu "Reported" menyaring baris grup dengan Reported lebih dari 0

### Status Tag Reported bersifat tambahan (TC-FA-TAG-614)

12. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
13. Verifikasi kolom Status baris Excavator 20 Ton - 20 menampilkan badge "Assigned" dan "Tag Reported" bersama-sama

### Report Type Missing lalu Report TAG hanya satu dari dua Tag (TC-FA-TAG-615 dan TC-FA-TAG-613)

14. Atur ulang data lewat fixture backend: Tag RF-00130 tanpa laporan terbuka hingga tersimpan
15. Ganti akun: logout dari akun Total Control [TC], login dengan akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], lalu buka modul Audit > Task Detail task Existence Audit, tab In Audit
16. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
17. Pilih Report Type "Missing"
18. Isi Textarea "Note" dengan "Tag hilang"
19. Klik [Submit]
20. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)
21. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
22. Centang hanya opsi "QR"
23. Pilih Report Type "Unreadable"
24. Isi Textarea "Note" dengan "QR pudar"
25. Klik [Submit]
26. Verifikasi toast "Success, TAG has been reported." tampil
27. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], login dengan akun Total Control [TC], lalu buka Global Settings > TAG
28. Cari Tag RF-00130: ketik Search "RF-00130", tekan Enter
29. Verifikasi Tag RF-00130 tetap berstatus Paired pada aset AST-0020

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-613 s.d. 616). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Report TAG satu Tag per Report Type dan dua Tag ada di spec 145 (TC-FA-TAG-609 s.d. 612).
- Urutan TC di dalam spec: TC-616 dan TC-614, TC-615, TC-613. TC-FA-TAG-614 dan TC-FA-TAG-616 memakai langkah submit yang identik (AST-0020, Report Type "Damaged", Note "Label retak"), sehingga satu submit (langkah 2 sampai 5) menjadi dasar kedua TC; verifikasi TC-616 (kartu, kolom, dan klik kartu) ditaruh sebelum membuka Popup Assets karena berada di halaman tabel grup, lalu TC-614 membuka Popup Assets. TC-615 dan TC-613 dijalankan sesudahnya dalam satu sesi Staff Auditor agar ganti akun tidak berulang. Perubahan urutan TC mengikuti pengelompokan sesi akun.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 dan 20 (menunggu aksi selesai sebelum ganti akun atau submit berikutnya), 7, 15, dan 27 (ganti akun eksplisit), serta 14 (mengatur ulang `RF-00130` tanpa laporan terbuka agar TC-615 dapat melaporkannya lagi). Search pada langkah 28 menemukan baris target (R-16).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - TC-FA-TAG-616 menulis "kartu Reported dan kolom Reported baris grup" bernilai N + 1 tanpa menyebut apakah N dibaca dari kartu global atau dari baris grup; spec mengasersi keduanya terhadap baseline N yang dicatat sebelum aksi.
  - Post Condition TC-FA-TAG-613 (laporan terbuka Unreadable dibuat untuk QR-00232 dan Tag RF-00132 tidak punya laporan) tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
