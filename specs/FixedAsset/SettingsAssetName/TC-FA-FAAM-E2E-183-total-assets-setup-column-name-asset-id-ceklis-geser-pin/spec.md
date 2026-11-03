---
id: TC-FA-FAAM-E2E-183-total-assets-setup-column-name-asset-id-ceklis-geser-pin
title: "Tab Total Assets Setup Column: Kelas Name dan Asset ID (Ceklis, Geser, Pin)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-528
  - TC-FA-FAAM-529
  - TC-FA-FAAM-530
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Kelas Name dan Asset ID (Ceklis, Geser, Pin)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kolom yang diuji pada ketiga TC: `Name` dan `Asset ID` (teks), dikerjakan berpasangan dalam satu penyimpanan per TC.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-528: Ceklis dan unceklis kelas Name, Asset ID (teks)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang `Name` dan `Asset ID`
3. Verifikasi Name: perubahan tampil di Live Preview (kolom tidak ada)
4. Verifikasi Asset ID: perubahan tampil di Live Preview (kolom tidak ada)
5. Klik `[Save]`
6. Verifikasi Name: perubahan tampil di tabel (kolom tidak tampil)
7. Verifikasi Asset ID: perubahan tampil di tabel (kolom tidak tampil)
8. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
9. Verifikasi Name: perubahan tersimpan dan tetap setelah popup dibuka kembali (kolom tetap tidak tampil)
10. Verifikasi Asset ID: perubahan tersimpan dan tetap setelah popup dibuka kembali (kolom tetap tidak tampil)
11. Klik header Actions (⋯), pilih `Setup Column...`, centang kembali `Name` dan `Asset ID`, klik `[Save]`
12. Verifikasi kolom Name dan Asset ID tampil kembali pada tabel

### TC-FA-FAAM-529: Geser urutan kelas Name, Asset ID (teks)

13. Klik header Actions (⋯), pilih `Setup Column...`, geser (drag) `Name` dan `Asset ID` ke posisi lain
14. Verifikasi Name: perubahan urutan tampil di Live Preview
15. Verifikasi Asset ID: perubahan urutan tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi Name: perubahan urutan tampil di tabel
18. Verifikasi Asset ID: perubahan urutan tampil di tabel
19. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
20. Verifikasi Name: urutan tersimpan dan tetap setelah popup dibuka kembali
21. Verifikasi Asset ID: urutan tersimpan dan tetap setelah popup dibuka kembali

### TC-FA-FAAM-530: Pin dan unpin kelas Name, Asset ID (teks)

22. Klik header Actions (⋯), pilih `Setup Column...`, klik icon Pin pada `Name` dan `Asset ID`
23. Verifikasi Name: perubahan pin tampil di Live Preview
24. Verifikasi Asset ID: perubahan pin tampil di Live Preview
25. Klik `[Save]`
26. Verifikasi Name: kolom ter-pin pada tabel
27. Verifikasi Asset ID: kolom ter-pin pada tabel
28. Tutup popup Detail, klik nama `Dell Latitude`, klik tab `Total Assets (42)`
29. Verifikasi Name: pin tersimpan dan tetap setelah popup dibuka kembali
30. Verifikasi Asset ID: pin tersimpan dan tetap setelah popup dibuka kembali
31. Klik header Actions (⋯), pilih `Setup Column...`, unpin `Name` dan `Asset ID`, klik `[Save]`
32. Verifikasi kolom Name dan Asset ID tidak lagi ter-pin pada tabel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas kolom Name dan Asset ID dikerjakan berpasangan dalam satu penyimpanan per TC; Expected per kolom (butir a untuk Name, butir b untuk Asset ID) masing-masing punya `Verifikasi`.
- Langkah penghubung: mencentang kembali kolom dan unpin sebagai pemulihan sebelum TC berikutnya (S-09); `Verifikasi` kolom tampil kembali dan tidak lagi ter-pin mengacu pada Expected "Perubahan tampil di tabel" untuk arah ceklis dan unpin. Urutan geser tidak dipulihkan di dalam spec; hook `after` menghapus preferensi kolom.
- Frasa "tersimpan per tabel di `localStorage`" pada Expected hanya teramati lewat kolom yang tetap sama setelah popup Detail dibuka kembali; media penyimpanan tidak diasersi (S-13). Aturan "pin maksimal tiga kolom" tidak diasersi karena TC tidak memberi langkah memin kolom keempat.
- Temuan untuk QA:
  - TC-FA-FAAM-528 sampai 530: Expected menyebut "Perubahan tampil di Live Preview dan tabel" tanpa menyebut bentuk perubahannya; spec mengasersi kolom tersembunyi, urutan baru, atau pin sesuai aksi.
