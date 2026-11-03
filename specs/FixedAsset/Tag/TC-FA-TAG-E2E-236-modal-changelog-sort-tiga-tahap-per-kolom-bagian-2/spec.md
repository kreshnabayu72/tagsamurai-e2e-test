---
id: TC-FA-TAG-E2E-236-modal-changelog-sort-tiga-tahap-per-kolom-bagian-2
title: "Modal Changelog Paired TAG: Sort Tiga Tahap Kolom Old Value, New Value, dan Modified By (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-946
  - TC-FA-TAG-947
  - TC-FA-TAG-948
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Sort Tiga Tahap Kolom Old Value, New Value, dan Modified By (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog Paired TAG dengan tanggal dan pelaku persis seperti tabel di bawah; tidak ada endpoint yang dikarang di spec ini. Changelog dalam scope akun Total Control hanya memuat E1 sampai E6 selama spec berjalan; fixture mengembalikan keadaan itu di hook `before` dan `after`, sehingga seluruh entri tampil pada halaman 1 (page size 10).
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Entri | Date | Action | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| E1 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [NFC] NF-00090 | [RFID] RF-00420 | Sari W. |
| E2 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [QR] QR-00240 | — | Sari W. |
| E3 | 26/10/26 09:20 | Replace | Excavator 20 Ton - 20 | TAG | [RFID] RF-00130 | [RFID] RF-00415 | Budi S. |
| E4 | 26/10/26 09:14 | Replace | Excavator 20 Ton - 42 | TAG | [QR] QR-00230 | [RFID] RF-00412 | Budi S. |
| E5 | 25/10/26 16:40 | Replace | Forklift Manual - 61 | TAG | [QR] QR-00251 | — | Dedi K. |
| E6 | 25/10/26 08:00 | Report TAG | Excavator 20 Ton - 20 | Report Type | — | Damaged | Rina T. |

  Kunci fixture: `changelogE1E6`.
- State yang diubah: hanya state sort modal; tiap kolom dikembalikan ke netral oleh klik ketiga. Tidak ada perubahan data bisnis.

## Test Steps

### Sort kolom Old Value (TC-FA-TAG-946)

1. Klik tombol `Changelog` pada Table Tools
2. Klik header Old Value sekali
3. Verifikasi Klik 1 (menaik): `[NFC] NF-00090` (E1), `[QR] QR-00230` (E4), `[QR] QR-00240` (E2), `[QR] QR-00251` (E5), `[RFID] RF-00130` (E3), lalu nilai kosong `—` (E6) di akhir
4. Klik header Old Value sekali lagi
5. Verifikasi Klik 2 (menurun): `—` (E6) di awal lalu urutan terbalik
6. Klik header Old Value sekali lagi
7. Verifikasi Klik 3 netral: kembali ke urutan bawaan

### Sort kolom New Value (TC-FA-TAG-947)

8. Klik header New Value sekali
9. Verifikasi Klik 1 (menaik): urutan relatif `[RFID] RF-00412` (E4), `[RFID] RF-00415` (E3), `[RFID] RF-00420` (E1), dengan nilai `—` (E2, E5) paling akhir
10. Klik header New Value sekali lagi
11. Verifikasi Klik 2 (menurun): `—` (E2, E5) di awal lalu urutan terbalik
12. Klik header New Value sekali lagi
13. Verifikasi Klik 3 netral: kembali ke urutan bawaan

### Sort kolom Modified By (TC-FA-TAG-948)

14. Klik header Modified By sekali
15. Verifikasi Klik 1 (A-Z menurut nama lengkap): Budi S. (E3, E4), Dedi K. (E5), Rina T. (E6), Sari W. (E1, E2)
16. Klik header Modified By sekali lagi
17. Verifikasi Klik 2 (Z-A): Sari W., Rina T., Dedi K., Budi S.
18. Klik header Modified By sekali lagi
19. Verifikasi Klik 3 netral: kembali ke urutan bawaan
20. Klik ikon close untuk menutup modal

## Notes

- Langkah penghubung (S-03): langkah 20 (menutup modal). Klik ketiga tiap kolom (langkah 6, 12, 18) mengembalikan sort ke netral, sehingga tiap blok kolom mulai dari urutan bawaan (S-09).
- Pembagian TC lintas spec: urutan bawaan serta sort kolom Date, Action, Name, dan Field (TC-FA-TAG-941 sampai TC-FA-TAG-945) ada di spec 235.
- Temuan untuk QA:
  - TC-FA-TAG-947 Expected a hanya menyebut urutan relatif tiga nilai `[RFID]` dan nilai `—` paling akhir (New Value E1 sampai E4); spec mengasersi hanya yang disebut TC.
  - TC-FA-TAG-948 mengurutkan "menurut nama lengkap" tetapi kolom menampilkan `[First Name] [Last Initial]`; spec mengasersi urutan nama yang tampil sesuai Expected TC.
  - Baris dengan nilai kolom sama (E2 dan E5 pada New Value; E1 dan E2 pada Modified By) tidak punya urutan pasti; spec tidak mengasersi urutan di antaranya.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi urutan bergantung pada Changelog yang hanya memuat E1 sampai E6, yang dijamin fixture backend (tim FE/BE).
