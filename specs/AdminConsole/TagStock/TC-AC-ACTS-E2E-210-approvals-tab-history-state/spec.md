---
id: TC-AC-ACTS-E2E-210-approvals-tab-history-state
title: "Approvals Tab History: State Kosong, Empty-Filtered, Error Load, dan Loading"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-647
  - TC-AC-ACTS-648
  - TC-AC-ACTS-649
  - TC-AC-ACTS-650
coverage:
  web: automated
---

# Approvals Tab History: State Kosong, Empty-Filtered, Error Load, dan Loading

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan intercept (disediakan tim FE): intercept respons 5xx dan penahan respons (delay jaringan) pada request daftar data Tab History, di atas backend nyata; endpoint tidak disebut TC dan tidak dikarang di spec. Intercept dilepas segera setelah dipakai (S-09).
- Data TC-AC-ACTS-647: kondisi Tab History tanpa Subject yang diputuskan disediakan fixture BE (disediakan tim FE/BE) dan riwayat dipulihkan lewat fixture BE di hook `after`; cara menyediakannya tidak disebut TC.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-648: Empty-filtered

2. Ketik Search `zzz-tidak-ada`, tekan Enter
3. Verifikasi ilustrasi empty state dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
4. Verifikasi tampilan bukan error
5. Klik `(←)` pada kotak Search

### TC-AC-ACTS-649: Error load fetch gagal bukan empty state

6. Aktifkan intercept respons 5xx pada request daftar data tabel
7. Muat ulang tampilan (F5)
8. Verifikasi copy `Unable to load this data.` dan tombol `[Try Again]` tampil di area tabel
9. Verifikasi tab bar dan toolbar tetap tampil
10. Verifikasi tampilan bukan empty state
11. Lepas intercept respons 5xx
12. Klik `[Try Again]`
13. Verifikasi tabel memuat ulang data (sedikitnya satu baris tampil)

### TC-AC-ACTS-650: Loading state

14. Aktifkan penahan respons daftar data (delay jaringan)
15. Muat ulang tampilan (F5)
16. Verifikasi komponen loading tampil selama data diambil
17. Lepas penahan respons
18. Verifikasi tabel menggantikan komponen loading

### TC-AC-ACTS-647: Empty state genuine

19. Siapkan kondisi tidak ada Subject yang diputuskan lewat fixture BE
20. Muat ulang tampilan (F5)
21. Verifikasi ilustrasi empty state dengan judul `No approval history yet` dan deskripsi `Processed approval requests will appear here.`
22. Verifikasi tidak ada baris data
23. Pulihkan riwayat Subject yang diputuskan lewat fixture BE

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Perubahan urutan TC (S-05): TC-AC-ACTS-648, 649, 650 dikerjakan lebih dulu pada Tab History berisi Subject, dan TC-AC-ACTS-647 di akhir sesudah kondisi riwayat kosong disiapkan lewat fixture BE.
- P-5 (butir b): TC-AC-ACTS-649 adalah objek uji ringan kelas b (satu kegagalan 5xx) pada permukaan yang sama dengan spec ini; intercept 5xx di atas backend nyata dan tidak ada TC kelas b lain di spec ini.
- Langkah penghubung (S-03): klik `(←)` pada kotak Search, melepas intercept dan penahan respons (S-09), memulihkan riwayat. Penahan respons pada TC-AC-ACTS-650 hanya untuk mengamati state Loading (bagian 3 prinsip 13b), diasersi sebelum dilepas (bagian 8b butir 5).
- Temuan untuk QA: TC-AC-ACTS-647 langkah 3 "Pastikan belum ada Subject yang diputuskan" bertentangan dengan precondition b (Tab History memuat sedikitnya 5 baris Subject); spec menyiapkan kondisi riwayat kosong lewat fixture BE yang disediakan tim FE/BE. Endpoint daftar untuk intercept (TC-AC-ACTS-649, 650) tidak disebut TC, PRD, atau LLD.
