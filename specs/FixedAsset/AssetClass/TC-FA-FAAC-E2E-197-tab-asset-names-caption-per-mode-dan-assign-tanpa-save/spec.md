---
id: TC-FA-FAAC-E2E-197-tab-asset-names-caption-per-mode-dan-assign-tanpa-save
title: "Tab Asset Names: Caption per Mode dan Assign pada Mode Edit Berlaku Tanpa Save"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-737
  - TC-FA-FAAC-736
  - TC-FA-FAAC-739
sourceRules: ["ST-37", "ST-05", "§4.1.3#p1", "§4.1.2#p1", "FAAC-LOGIC-13b", "T-07"]
smoke: []
dependsOn: []
trace:
  "ST-37": [4, 9]
  "ST-05": 3
  "§4.1.3#p1": [4, 9, 10]
  "§4.1.2#p1": [17, 18, 21]
  "FAAC-LOGIC-13b": [15, 21]
  "T-07": 15
coverage:
  web: automated
---

# Tab Asset Names: Caption per Mode dan Assign pada Mode Edit Berlaku Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` suite; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API, dihapus di hook `after`; kode literal, lihat Notes): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-197`, Class Name `Anchor Class {runId}-197` (disebut "anchor").
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE ke tanpa Asset Class di hook `before` dan `after`): Asset Name Meeting Table (0 aset aktif). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE (lihat `suite.md`, butir Seed dan pemulihan).
- State global: keanggotaan Meeting Table berubah oleh langkah 13; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-737: Caption tab Asset Names tidak tampil pada Detail mode Add Asset Class

1. Klik tombol "+ Asset Class" di toolbar tabel
2. Klik tab "Asset Names"
3. Verifikasi tombol "+ Assign Asset Names" tampil dan Enabled
4. Verifikasi caption "Changes on this tab are applied immediately." tidak tampil di bawah judul SectionCard tabel
5. Klik breadcrumb "Asset Class"

### TC-FA-FAAC-736: Caption tab Asset Names tampil pada Detail mode Edit

6. Ketik Search `ANCHOR-197`, tekan Enter
7. Klik link Class Code `ANCHOR-197`
8. Klik tab "Asset Names"
9. Verifikasi caption "Changes on this tab are applied immediately." tampil di bawah judul SectionCard tabel
10. Verifikasi tombol "+ Assign Asset Names" tampil

### TC-FA-FAAC-739: Assign pada Detail mode Edit berlaku tanpa Save dan tidak membuat form dirty

11. Klik tombol "+ Assign Asset Names"
12. Centang baris "Meeting Table"
13. Klik [Assign]
14. Verifikasi dialog Assign Asset Names menutup
15. Verifikasi muncul toast sukses: "Success, asset name has been assigned."
16. Klik breadcrumb "Asset Class" tanpa mengubah field apa pun dan tanpa klik [Save]
17. Verifikasi tabel Asset Class tampil
18. Verifikasi dialog Unsaved Changes tidak tampil
19. Ganti isi kotak Search dengan `ANCHOR-197`, tekan Enter
20. Klik link Class Code `ANCHOR-197`, lalu klik tab "Asset Names"
21. Verifikasi "Meeting Table" tercantum di tabel tab Asset Names

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 737, 736, 739. TC-737 dijalankan lebih dulu karena form Create dibuka dan ditinggalkan tanpa isian; TC-739 terakhir karena mengubah keanggotaan Meeting Table.
- Class Code `ANCHOR-197` ditulis literal tanpa suffix `{runId}-<NNN>` karena Class Code dibatasi 15 karakter sehingga suffix itu tidak muat (S-12, nama literal; pola spec 067 dan 068); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu.
- Pengecualian nama literal (S-06, S-12): Asset Name Meeting Table adalah seed Pre-setup yang dipakai apa adanya; pemulihan oleh fixture BE di hook `after`.
- Langkah penghubung (S-03): langkah 5 (keluar dari form Create yang belum diisi), langkah 6 dan 19 (Search baris anchor, 8b.13; kotak Search dipertahankan sesudah kembali dari Detail, 8b.9), langkah 7, 8, dan 20 (navigasi).
- Langkah 4 dan 18 adalah asersi absence; anchor positifnya langkah 3 (tombol pada tab yang sama) dan langkah 17 (tabel tujuan navigasi tampil) (8b.2). Dialog Unsaved Changes tidak pernah diharapkan muncul pada alur ini, sehingga anchornya adalah layar tujuan navigasi.
- Langkah 21 membuka ulang Detail untuk membuktikan Assign tersimpan tanpa `[Save]` (Expected c TC-739).
