---
id: TC-FA-TAG-E2E-169-decline-report-tag-declined-dapat-dilaporkan-ulang
title: "Decline Report: Tag Declined Dapat Dilaporkan Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-644
coverage:
  web: automated
---

# Decline Report: Tag Declined Dapat Dilaporkan Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |

- Akun aktor pertama: Total Control [TC]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Langkah ganti akun ditulis eksplisit (Logout lalu Login). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |

- State yang diubah dan pemulihannya: laporan Declined dan laporan baru Missing pada `RF-00130` dipulihkan lewat fixture backend di hook `after`; spec selesai di akun Staff Auditor dan hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 12); entri Changelog `Decline Report` per Tag (langkah 5).

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Klik tombol [Submit]
6. Tunggu aksi selesai (dialog "Decline Report" tertutup dan tombol aktif kembali)
7. Ganti akun: logout dari akun Total Control [TC], login dengan akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], lalu buka modul Audit > Task Detail task Existence Audit, tab In Audit
8. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
9. Verifikasi dialog "Report TAG" menerima RF-00130 (opsi tidak Disabled)
10. Pilih Report Type "Missing"
11. Isi Textarea "Note" dengan "Hilang lagi"
12. Klik tombol [Submit]
13. Verifikasi toast "Success, TAG has been reported." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-644). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Decline Report satu pengguna ada di spec 151 sampai 153 dan konflik pengguna lain di spec 154.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 (menunggu aksi selesai sebelum ganti akun) dan 7 (ganti akun eksplisit).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 12); entri Changelog `Decline Report` per Tag (langkah 5).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-644 ("Laporan baru Missing terbuka untuk RF-00130 dan laporan lama tetap berstatus Declined") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
