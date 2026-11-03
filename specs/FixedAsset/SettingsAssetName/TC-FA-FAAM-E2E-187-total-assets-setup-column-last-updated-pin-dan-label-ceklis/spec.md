---
id: TC-FA-FAAM-E2E-187-total-assets-setup-column-last-updated-pin-dan-label-ceklis
title: "Tab Total Assets Setup Column: Last Updated Pin dan Kelas Label (Default Tersembunyi, Ceklis)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-539
  - TC-FA-FAAM-714
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Last Updated Pin dan Kelas Label (Default Tersembunyi, Ceklis)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26). Setiap aset berlabel `Finance` dan `High Priority`, aset `Dell Latitude - 42` berlabel tambahan `Fragile`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kolom yang diuji: `Last Updated` (pin, TC-FA-FAAM-539) dan `Label` (kolom curated, TC-FA-FAAM-714).
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-539: Pin dan unpin kelas Last Updated (tanggal)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, klik icon Pin pada `Last Updated`
3. Verifikasi perubahan pin tampil di Live Preview
4. Klik `[Save]`
5. Verifikasi kolom Last Updated ter-pin pada tabel
6. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
7. Verifikasi pin tersimpan dan tetap setelah popup dibuka kembali
8. Klik header Actions (⋯), pilih `Setup Column...`, unpin `Last Updated`, klik `[Save]`
9. Verifikasi kolom Last Updated tidak lagi ter-pin pada tabel

### TC-FA-FAAM-714: Kelas Label (curated): default tersembunyi, ceklis dan unceklis

10. Amati header kolom tabel
11. Verifikasi pada kondisi default kolom Label tidak tampil di tabel
12. Klik header Actions (⋯), pilih `Setup Column...`
13. Verifikasi di Popup Setup Column Label `☐ Curated` (unchecked, enabled)
14. Centang Label
15. Verifikasi kolom Label tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi kolom Label tampil di tabel
18. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
19. Verifikasi pilihan tersimpan dan tetap setelah popup dibuka kembali (kolom Label tetap tampil)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 539 sebelum 714 (539 mengasersi kolom default sebagai titik awal; 714 menyimpan Label sebagai kolom tampil).
- Langkah penghubung: unpin sebagai pemulihan (S-09); `Verifikasi` kolom tidak lagi ter-pin mengacu pada Expected "Perubahan tampil di tabel".
- "tersimpan per tabel di `localStorage`" hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali (S-13); "pin maksimal tiga kolom" tidak diasersi karena TC tidak memberi langkah memin kolom keempat.
