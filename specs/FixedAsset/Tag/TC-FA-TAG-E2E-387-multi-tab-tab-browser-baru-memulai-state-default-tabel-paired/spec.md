---
id: TC-FA-TAG-E2E-387-multi-tab-tab-browser-baru-memulai-state-default-tabel-paired
title: "Multi-Tab: Tab Browser Baru Memulai State Default Tabel Paired"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-929
coverage:
  web: automated
---

# Multi-Tab: Tab Browser Baru Memulai State Default Tabel Paired

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini pada tab pertama; halaman dibuka hook `beforeEach` suite.
- Konteks: satu konteks browser dengan dua tab. Tab pertama adalah sesi login hook `before`; tab kedua dibuka pada langkah 2 dengan sesi login yang sama (tanpa login terpisah) dan menjadi objek asersi (langkah 3 dan 4). Tab kedua ditutup pada langkah 5; hook `after` menutupnya bila spec gagal sebelum langkah itu.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): tab browser kedua dengan sesi yang sama (konteks yang sama dengan sesi login, tanpa login terpisah); seed dan pemulihan idempotent lewat fixture backend untuk dataset tab Paired di bawah; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup tab Paired, dataset umum empat grup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup acuan | Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupAcuan` |

- State yang diubah: hanya state tampilan tab pertama (Search); tidak ada perubahan data bisnis. Search dikosongkan oleh langkah 6.

## Test Steps

### Tab browser baru memulai state default (TC-FA-TAG-929)

1. Ketik Search `Forklift`, tekan Enter
2. Buka halaman TAG pada tab browser baru
3. Verifikasi tab browser baru menampilkan empat baris grup
4. Verifikasi tab browser baru tidak memuat Search
5. Tutup tab browser baru dan kembali ke tab pertama
6. Klik `(←)` pada kotak Search

## Notes

- Spec multi-konteks (kelas c, prinsip 13c): tab browser kedua adalah objek asersi (langkah 3 dan 4), bukan pemicu state; karena itu TC-FA-TAG-929 dipisah dari spec fungsional 242 dan tidak memakai pengecualian `P-2`. Jenis harness satu: multi-tab dalam satu konteks browser; tidak ada dua tenant, dua admin, atau flood rate-limit.
- Pembagian TC lintas spec: TC-FA-TAG-925 sampai TC-FA-TAG-928 ada di spec 231 dan TC-FA-TAG-930 (state tabel sesudah kembali dari halaman lain) ada di spec 242.
- Langkah penghubung (S-03): langkah 5 (menutup tab browser baru dan kembali ke tab pertama) dan 6 (mengosongkan Search lewat `(←)`).
- Anchor positif absence (bagian 8b butir 2): langkah 3 (empat baris grup tampil di tab baru) mendahului langkah 4 (tab baru tidak memuat Search), sehingga hasil tanpa Search bukan karena tabel belum dimuat.
- Dataset memakai empat grup umum (precondition TC-FA-TAG-929 dan Expected "empat baris grup"), bukan dataset khusus 25 grup milik spec 229 dan 231.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-929 ("Tidak ada perubahan data bisnis (aksi hanya membaca)") tidak punya langkah observasi dan tidak diasersi.
