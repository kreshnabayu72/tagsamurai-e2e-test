---
id: TC-FA-TDC-E2E-277-picker-tax-method-asset-class-disabled-dan-tooltip-karena-versi-scheduled
title: "Picker Tax Method Asset Class: Metode yang Dibuang Versi Scheduled Disabled dengan Tooltip"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-966
sourceRules: ["S-03g", "FATDC-LOGIC-10c", "D-08", "D-09"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-10c": [4, 5, 10]
  "D-08": 5
  "D-09": 4
  "S-03g": [17, 18, 20]
coverage:
  web: automated
---

# Picker Tax Method Asset Class: Metode yang Dibuang Versi Scheduled Disabled dengan Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class dan Asset Class pemakai lewat API; pemulihan data lewat API; mengarahkan kursor pada opsi dropdown untuk tooltip (langkah 19); tombol `Esc` (langkah 21).
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat):

| Kunci fixture (usulan) | Class Code | Keterangan |
|---|---|---|
| `khsV19` | `KHS-V19` | Non-building, Useful Life 8, Straight Line dan Declining Balance, Used By 1: Asset Class `AC-SCH5 – Alat Berat` memakai Straight Line (kunci `assetClassAlatBerat`, disediakan tim FE/BE) |

- Tabel memuat tujuh class seed bawaan dan satu class milik spec (8 baris dalam satu halaman) sehingga baris target dibuka tanpa Search (8b.13, R-23).
- State global yang diubah: jam server dan jam browser (hook `before`, dipulihkan di `after`) dan versi Scheduled Jan 2027 `KHS-V19` (dibentuk langkah 7, dihapus lewat seeding ulang di hook `after`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-966: Versi Scheduled yang mempersempit Allowed Methods membuat metode yang dibuang Disabled pada picker Tax Method Asset Class

1. Klik link Class Code `KHS-V19` pada tabel
2. Lepas `Declining Balance` dari Allowed Methods
3. Klik `[Save]`
4. Verifikasi dialog Save Changes dengan field Effective From tampil
5. Verifikasi dialog "Cannot Remove This Method" tidak tampil
6. Pilih Effective From `Jan 2027`
7. Klik `[Apply]` hingga versi berhasil tersimpan
8. Klik link Class Code `KHS-V19` pada tabel
9. Klik tautan View versions
10. Verifikasi versi `Jan 2027` berstatus `Scheduled`
11. Tutup modal Versions
12. Klik `[×]` pada header Drawer
13. Klik tab Asset Class
14. Ketik Search `AC-SCH5`, tekan Enter
15. Buka Drawer Edit Asset Class AC-SCH5
16. Klik dropdown Tax Method
17. Verifikasi opsi `Straight Line` dapat dipilih
18. Verifikasi opsi `Declining Balance` Disabled
19. Arahkan kursor ke opsi `Declining Balance`
20. Verifikasi tooltip `Not allowed from Jan 2027.`
21. Tekan `Esc` untuk menutup dropdown Tax Method
22. Klik `[×]` pada header Drawer Edit Asset Class
23. Klik tab Tax Depreciation Class

## Notes

- Langkah penghubung (S-03): langkah 8 sampai 12 (membuka Drawer lagi untuk mengamati versi Scheduled lewat Modal Versions; TC hanya menulis "versi Scheduled Jan 2027 terbentuk"), langkah 11 (menutup modal), langkah 12 dan 22 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`), langkah 13 dan 23 (berpindah tab), langkah 14 (Search `AC-SCH5` untuk menemukan baris target; R-16), langkah 21 (menutup dropdown tanpa memilih opsi).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 adalah anchor positif untuk asersi absence langkah 5 ("Save lolos", 8b.2); langkah 17 (opsi `Straight Line` dapat dipilih) adalah Expected b TC dan anchor bahwa dropdown terbuka sebelum asersi Disabled langkah 18.
- Pemilik perilaku picker (Disabled dan tooltip `Not allowed from [MMM YYYY].`) adalah modul Asset Class (FAAC-LOGIC-02f); spec ini menguji pengaruh versi Scheduled class pada picker tersebut seperti TC-966.
- Asumsi: sesudah `[Apply]` (langkah 7) Drawer tertutup, sehingga langkah 8 membuka Drawer lagi; perlu konfirmasi FE.
- TC-967 (pemulihan picker sesudah Cancel Scheduled Version) ada di spec 278.
- Temuan untuk QA:
  - TC-966 tidak menyebut cara menutup dropdown dan Drawer Edit Asset Class sesudah asersi; spec memakai `Esc` dan `[×]` tanpa perubahan.
  - TC-966 tidak menyebut cara membuka Drawer Edit Asset Class; spec menulis "Buka Drawer Edit" tanpa label tombol, perlu dilengkapi dari PRD Asset Class.
  - TC-966 Expected a ("versi Scheduled Jan 2027 terbentuk") tanpa tempat mengamati; spec memakai Modal Versions (langkah 8 sampai 11).
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
