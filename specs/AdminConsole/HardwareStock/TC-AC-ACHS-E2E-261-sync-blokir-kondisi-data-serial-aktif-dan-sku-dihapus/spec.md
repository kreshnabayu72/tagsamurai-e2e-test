---
id: TC-AC-ACHS-E2E-261-sync-blokir-kondisi-data-serial-aktif-dan-sku-dihapus
title: "Sync Diblokir Kondisi Data: Serial Aktif dan SKU Dihapus"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-142
  - TC-AC-ACHS-152
coverage:
  web: automated
---

# Sync Diblokir Kondisi Data: Serial Aktif dan SKU Dihapus

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal {accTc} `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{accTc}` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `{skuStaleHh}` | #16d | kode SKU Handheld Reader tanpa unit yang dibuat khusus untuk TC stale | `Fixture.hardwareStock.p16d.handheldSku` |
| `{skuRfd}` | #16, #17, #18 (Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 18 Available dan 7 In Use | `Fixture.hardwareStock.p16.a[4].sku` |
| `{snRfdAvail}` | #17 (Tabel E baris N = 10) | Serial Number unit Available pertama pada skuRfd | `Fixture.hardwareStock.p17.e[10].serialNumber` |

- Data Pre-setup: SKU `{skuRfd}` dengan unit Available `{snRfdAvail}` (hanya dibaca, Pre-setup #17); SKU `{skuStaleHh}` (Handheld Reader, tanpa unit, Pre-setup #16d); service driver mock (Pre-setup #25). Hook `before` memastikan SKU stale ada dan hook `after` membuatnya kembali bila dihapus spec.
- Data Dinamis: perangkat simulasi `SN-ZEBRA-RFD40-100101-{runId}-261` (TC-142) dan `SN-STALE-910001-{runId}-261` (TC-152); tidak ada yang tersimpan.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader USB Pre-setup #25; sesi API aktor yang menghapus SKU (padanan "sesi lain" TC-152; endpoint tidak disebut TC, PRD, atau LLD, S-13).
- State global: SKU `{skuStaleHh}` dihapus pada langkah 26; dipulihkan di hook `after`.

## Test Steps

### TC-AC-ACHS-142: Keunikan serial aktif menolak seluruh Submit

1. Ketik Search `{skuRfd}`, tekan Enter
2. Klik row action `Detail` pada baris SKU `{skuRfd}`
3. Catat Total Registered dan Available pada Summary bar sebagai baseline
4. Klik segmen `Stock` pada breadcrumb
5. Ketik Search `{skuRfd}`, tekan Enter
6. Klik `(⋯)` pada baris SKU `{skuRfd}`
7. Klik opsi `Add Stock`
8. Atur simulator: perangkat `{snRfdAvail}` (unit Available SKU yang sama)
9. Klik `[Sync]`
10. Atur simulator: perangkat `SN-ZEBRA-RFD40-100101-{runId}-261` (OK)
11. Klik `[Sync]`
12. Klik `[Submit]`
13. Klik `[Continue]` pada dialog konfirmasi
14. Verifikasi error banner "Serial number {snRfdAvail} already exists in the system" menolak seluruh Submit
15. Verifikasi badge Status baris Sync tidak berubah
16. Klik `[Cancel]`
17. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
18. Klik `[Leave]`
19. Verifikasi Summary bar Total Registered dan Available sama dengan baseline langkah 3 (tidak ada unit tersimpan, termasuk `SN-ZEBRA-RFD40-100101-{runId}-261`)

### TC-AC-ACHS-152: SKU dihapus sesi lain sebelum Submit Sync

20. Klik segmen `Stock` pada breadcrumb
21. Ketik Search `{skuStaleHh}`, tekan Enter
22. Klik `(⋯)` pada baris SKU `{skuStaleHh}`
23. Klik opsi `Add Stock`
24. Atur simulator: perangkat `SN-STALE-910001-{runId}-261`
25. Klik `[Sync]`
26. Hapus SKU `{skuStaleHh}` lewat sesi API aktor hingga SKU terhapus
27. Klik `[Submit]`
28. Verifikasi error banner "This SKU no longer exists. Go back to the Stock List and try again."
29. Verifikasi `[Submit]` disabled
30. Verifikasi tabel Synced Units tetap berisi `SN-STALE-910001-{runId}-261`
31. Klik `(⋯)` pada baris pertama tabel Synced Units, lalu klik `Remove` (kembalikan form ke nilai tersimpan: 0 baris)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-142, 152). Tidak ada TC hanya-BE di spec ini.
- Kasus blokir karena kondisi data (prinsip 12). Pelaku "sesi lain" TC-152 memakai sesi API aktor (tanpa `P-2`); kata "Manual Only" pada kolom Automation bukan alasan mengeluarkan TC.
- Spec berakhir dengan form dirty pada langkah 30; langkah 31 mengembalikan field ke nilai tersimpan (S-09) karena `[Leave]` mendarat di Tab Available SKU yang sudah terhapus.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search (langkah 1, 5, 21), baseline (langkah 3), pengaturan simulator (langkah 8, 10, 24), `[Continue]` (langkah 13), dan pemicu langkah 26.
- Temuan untuk QA:
  - TC-142 menyebut dialog dikonfirmasi dengan `[Continue]` tanpa menyebut varian dialog D-02; di TC-133 unit In Use pada SKU yang sama menjadi `Waiting for Approval` dan bukan hard block, sedangkan TC-142 judul menyebut "Available/In Use" ditolak. Spec mengikuti TC-142 (unit Available) dan hanya menguji unit Available.
  - TC-142 butir b ("badge Sync tidak berubah") tidak menyebut badge yang dimaksud; spec memakai badge Status baris.
  - TC-142 dan TC-152 tidak memuat Post Condition.
