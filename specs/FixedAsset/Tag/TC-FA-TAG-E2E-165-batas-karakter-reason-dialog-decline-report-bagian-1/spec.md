---
id: TC-FA-TAG-E2E-165-batas-karakter-reason-dialog-decline-report-bagian-1
title: "Batas Karakter Reason Dialog Decline Report (Bagian 1)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1392
  - TC-FA-TAG-1393
  - TC-FA-TAG-1394
coverage:
  web: automated
---

# Batas Karakter Reason Dialog Decline Report (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Akun aktor pertama: Total Control [TC]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |

- State yang diubah dan pemulihannya: laporan `RF-00130` yang ditutup (Declined) oleh spec ini dan yang diatur ulang dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 16, 25). Aksi tulis pada langkah 6 ditolak dan tidak menambah entri.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Reason 361 karakter ditolak (TC-FA-TAG-1393)

2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan teks 361 karakter (huruf `a` diulang 361 kali)
5. Verifikasi pesan error "Max. 360 characters" tampil pada Textarea "Reason" langsung setelah teks diisi
6. Klik tombol [Submit]
7. Verifikasi [Submit] diblok selama error masih tampil (tidak ada toast sukses dan error "Max. 360 characters" masih tampil)
8. Verifikasi dialog "Decline Report" tetap terbuka
9. Klik ikon close pada header dialog "Decline Report"
10. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
11. Klik [Leave]

### Reason tepat 360 karakter diterima (TC-FA-TAG-1392)

12. Buka menu aksi baris Excavator 20 Ton - 20
13. Klik "Decline Report"
14. Isi Textarea "Reason" dengan teks 360 karakter (huruf `a` diulang 360 kali)
15. Verifikasi tidak ada pesan error "Max. 360 characters" pada Textarea "Reason"
16. Klik tombol [Submit]
17. Verifikasi dialog "Decline Report" menutup
18. Verifikasi toast "Success, report has been declined." tampil

### Reason 360 karakter dengan kelebihan spasi di ujung (TC-FA-TAG-1394)

19. Atur ulang data lewat fixture backend: Tag RF-00130 laporan terbuka Damaged dari Staff Auditor hingga tersimpan, lalu muat ulang halaman
20. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
21. Buka menu aksi baris Excavator 20 Ton - 20
22. Klik "Decline Report"
23. Isi Textarea "Reason" dengan teks 360 karakter (huruf `a` diulang 360 kali) diikuti 10 spasi di akhir
24. Verifikasi tidak ada pesan error "Max. 360 characters" karena panjang dihitung setelah trim
25. Klik tombol [Submit]
26. Verifikasi dialog "Decline Report" menutup
27. Verifikasi toast "Success, report has been declined." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1392 s.d. 1394). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Reason yang hanya berisi spasi pada dialog Decline Report (TC-FA-TAG-1395) ada di spec 166.
- Urutan TC di dalam spec: TC-1393, TC-1392, TC-1394. Validasi yang diblokir dijalankan sebelum Submit yang berhasil; laporan `RF-00130` diatur ulang sebelum TC-1394 karena TC-1392 sudah menutupnya (langkah 19).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 sampai 11 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]) dan 19 (mengatur ulang state laporan lewat fixture backend; muat ulang halaman juga menghilangkan toast sebelumnya).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 16, 25). Aksi tulis pada langkah 6 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Panjang teks dihitung setelah trim sesuai Expected TC; nilai 360 dan 361 karakter ditulis tepat sebagai huruf `a` yang diulang tanpa suffix karena asersi bergantung pada panjang persis.
  - Post Condition TC-FA-TAG-1392 s.d. 1394 (laporan RF-00130 berstatus Declined atau tetap terbuka) tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
