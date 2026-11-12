---
id: TC-FA-TAG-E2E-166-batas-karakter-reason-dialog-decline-report-bagian-2
title: "Batas Karakter Reason Dialog Decline Report (Bagian 2)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1395
coverage:
  web: automated
---

# Batas Karakter Reason Dialog Decline Report (Bagian 2)

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

- State yang diubah dan pemulihannya: tidak ada laporan yang ditutup oleh spec ini; data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan lima spasi saja (tanpa karakter lain)
5. Klik tombol [Submit]
6. Verifikasi pesan error "Reason must not be empty" tampil pada Textarea "Reason" karena isian dihitung kosong setelah trim
7. Verifikasi dialog "Decline Report" tetap terbuka
8. Verifikasi tidak ada toast sukses
9. Kosongkan Textarea "Reason"
10. Klik ikon close pada header dialog "Decline Report"

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1395). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: batas karakter Reason Decline Report (TC-FA-TAG-1392 s.d. 1394) ada di spec 165.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 sampai 10 (memulihkan Reason yang hanya berisi spasi dengan mengosongkannya lalu menutup dialog).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - Panjang teks dihitung setelah trim sesuai Expected TC; nilai 360 dan 361 karakter ditulis tepat sebagai huruf `a` yang diulang tanpa suffix karena asersi bergantung pada panjang persis.
  - Post Condition TC-FA-TAG-1395 ("Laporan RF-00130 tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
