---
id: TC-GS-GSET-E2E-017-screening-modal-changelog-dan-pagination
title: Screening Modal Changelog dan kontrol pagination
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-41
  - TC-GS-GSET-153
coverage:
  web: automated
---

# Screening Modal Changelog dan kontrol pagination

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Ada riwayat perubahan (>100 baris) untuk membuktikan pagination
  (`Fixture.globalSettingsGeneralSettings.logs.many`).
- Modal Changelog dibuka dari Icon Button `Changelog` di header halaman.

## Test Steps

### Screening 3 zona modal

1. Buka halaman `Global Settings > General Settings`
2. Klik Icon Button `Changelog` di header halaman
3. Verifikasi modal menampilkan 3 zona: Header, Toolbar, dan Content/Footer tabel
4. Verifikasi zona Header menampilkan title `Changelog: General Settings`
5. Verifikasi zona Toolbar menampilkan (`Search`, `Filter`, `Download`) dan tombol `[✕]`
6. Verifikasi placeholder search `Search action, field, or value...`

### Screening 7 kolom

7. Verifikasi tabel menampilkan kolom secara berurutan:
   `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, `Actions (⋯)`
8. Verifikasi kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` dapat di-sort
   (indikator sort/header klik)
9. Verifikasi kolom `Actions (⋯)` TIDAK dapat di-sort: klik header-nya membuka Setup Column, dan sel
   body per baris kosong/read-only
10. Verifikasi setiap baris `Action` selalu bertulisan `Edit`
11. Verifikasi default sort adalah `Date` descending (baris terbaru di atas)

### Header colomn & pagination

12. Verifikasi header kolom `⋯` (Column Visibility / Setup Column) tampil
13. Verifikasi footer pagination menampilkan jumlah baris, halaman saat ini, dan total halaman, default
    page size `10`
14. Verifikasi kontrol pemilih page size menampilkan opsi persis `10`, `25`, `50`, `100`
15. Pilih `25`: verifikasi tabel menampilkan maksimal 25 baris dan pagination menyesuaikan
16. Pilih `50` dan `100` berturut-turut: verifikasi jumlah baris mengikuti pilihan, dimulai dari
    halaman 1
17. Klik halaman berikutnya/halaman tertentu: verifikasi baris berubah dan info halaman aktif
18. Verifikasi transisi halaman menjaga posisi scroll/state footer tetap utuh
19. Tutup modal via `[✕]`

## Notes

- Page size dan jumlah baris mengikuti data yang tersedia; verifikasi berhenti pada kesesuaian kontrol
  pagination dengan jumlah data yang sebenarnya.
- Kolom `Actions (⋯)` pada modal changelog ini berbeda dari tabel CRUD: di sini ia read-only tanpa
  aksi baris (spec 041/41 menjadi acuan). Modal yang dikosongkan datanya dibahas di spec 018.