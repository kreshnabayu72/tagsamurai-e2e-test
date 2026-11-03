---
id: TC-AC-ACHS-E2E-254-blokir-kondisi-data-sku-dihapus-add-stock-manual
title: "Blokir Kondisi Data: SKU Dihapus Sebelum Submit Add Stock Manual"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-97
coverage:
  web: automated
---

# Blokir Kondisi Data: SKU Dihapus Sebelum Submit Add Stock Manual

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuStale}` | #16d | kode SKU Smart Fixed Reader tanpa unit yang dibuat khusus untuk TC stale | `Fixture.hardwareStock.p16d.sfrSku` |

- Data Pre-setup: SKU `{skuStale}` (Smart Fixed Reader, tanpa unit; Pre-setup #16d, dibuat khusus untuk TC stale). Hook `before` memastikan SKU ini ada (seeding idempotent) dan hook `after` membuatnya kembali bila sudah dihapus spec.
- Data Dinamis: `SN-STALE-0001` diketik tetapi tidak pernah tersimpan (literal seperti di TC).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor yang menghapus SKU di Settings > Device > SKU (padanan "sesi lain" di TC-97; endpoint tidak disebut TC, PRD, atau LLD, S-13); membaca daftar unit SKU lewat fixture BE untuk membuktikan tidak ada unit tersimpan (Expected TC-97 butir c); pembuatan ulang SKU stale di hook `after`.
- State global: SKU `{skuStale}` dihapus pada langkah 4; dipulihkan di hook `after`.

## Test Steps

1. Ketik Search `{skuStale}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuStale}`
3. Klik opsi `Add Stock`
4. Hapus SKU `{skuStale}` lewat sesi API aktor hingga SKU terhapus
5. Ketik `SN-STALE-0001` di textarea
6. Klik `[Submit]`
7. Verifikasi error banner "This SKU no longer exists. Go back to the Stock List and try again."
8. Verifikasi `[Submit]` menjadi disabled
9. Verifikasi isi textarea `SN-STALE-0001` dipertahankan
10. Verifikasi lewat fixture BE bahwa tidak ada unit `SN-STALE-0001` tersimpan
11. Kosongkan isi textarea (kembalikan field ke nilai tersimpan)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-97). Tidak ada TC hanya-BE di spec ini.
- Kasus blokir karena kondisi data jadi spec sendiri (prinsip 12 bagian 3). Pelaku "sesi lain" TC-97 memakai sesi API aktor (pelaku kedua yang hanya mengubah state; tanpa `P-2`). Kata "Manual Only" pada kolom Automation bukan alasan mengeluarkan TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1), langkah 4 (memicu kondisi), dan langkah 11: spec berakhir dengan form dirty (textarea berisi `SN-STALE-0001`), sehingga dipulihkan dengan mengosongkan field ke nilai tersimpan (S-09). Menutup form lewat `[Cancel]` dan `[Leave]` tidak dipakai karena `[Leave]` mendarat di Tab Available SKU yang sudah dihapus.
- Langkah 10 membuktikan Expected butir c lewat kemampuan baca BE karena SKU yang dihapus tidak lagi tampil di UI (S-11).
- Temuan untuk QA:
  - TC-97 tidak menyebut cara mengamati "tidak ada unit tersimpan" untuk SKU yang sudah terhapus; spec memakai kemampuan baca fixture BE (disediakan tim FE/BE).
  - TC-97 tidak memuat Post Condition.
