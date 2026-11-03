---
id: TC-FA-TAG-E2E-242-state-tabel-refresh-tab-sidebar-dan-kembali-bagian-2
title: "State Tabel Paired: Tab Browser Baru dan Kembali dari Halaman Lain (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-929
  - TC-FA-TAG-930
coverage:
  web: automated
---

# State Tabel Paired: Tab Browser Baru dan Kembali dari Halaman Lain (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk dataset tab Paired di bawah; tab browser kedua dengan sesi yang sama (konteks yang sama dengan sesi login, tanpa login terpisah); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup tab Paired (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup acuan | Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupAcuan` |
| Aset untuk Asset Detail | Aset 'Excavator 20 Ton - 20' (AST-0020) pada grup Excavator 20 Ton / Plant B | `aset20` |

- State yang diubah: hanya state tampilan tabel (Search dan Sort); tidak ada perubahan data bisnis. Search dan Sort dipulihkan oleh langkah 6, 13, dan 14.

## Test Steps

### Tab browser baru memulai state default (TC-FA-TAG-929)

1. Ketik Search `Forklift`, tekan Enter
2. Buka halaman TAG pada tab browser baru
3. Verifikasi tab browser baru menampilkan empat baris grup
4. Verifikasi tab browser baru tidak memuat Search
5. Tutup tab browser baru dan kembali ke tab pertama
6. Klik `(←)` pada kotak Search

### Kembali dari halaman lain mempertahankan state (TC-FA-TAG-930)

7. Ketik Search `Ton`, tekan Enter
8. Klik header Total Assets sekali
9. Buka Asset Detail aset 'Excavator 20 Ton - 20' (AST-0020) dari Popup Detail grup Excavator 20 Ton pada baris Plant B
10. Klik Breadcrumb `TAG` untuk kembali ke halaman TAG
11. Verifikasi Search `Ton` tetap aktif
12. Verifikasi sort Total Assets menaik tetap aktif
13. Klik `(←)` pada kotak Search
14. Klik header Total Assets dua kali lagi hingga sort netral

## Notes

- Langkah penghubung (S-03): langkah 5 (menutup tab browser baru), 6 dan 13 (mengosongkan Search lewat `(←)`), dan 14 (mengembalikan sort ke netral).
- Pembagian TC lintas spec: TC-FA-TAG-925 sampai TC-FA-TAG-928 ada di spec 231.
- Temuan untuk QA:
  - TC-FA-TAG-929 Expected "empat baris grup" bertentangan dengan Data Uji TC-FA-TAG-925 pada spec 231 ("scope memuat total 25 baris grup", page size bawaan 10); spec mengikuti teks TC (langkah 3).
  - TC-FA-TAG-930 langkah 3 "Buka Asset Detail salah satu aset" tidak menyebut jalur pembukaan Asset Detail dan teks segmen Breadcrumb untuk kembali; spec memakai Popup Detail dan segmen `TAG` dari Breadcrumb `Fixed Asset > TAG > Paired`. Aset yang dibuka dipilih oleh spec ('Excavator 20 Ton - 20').
  - Post Condition kedua TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
