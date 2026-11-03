---
id: TC-AC-RP-E2E-084-picker-kolom-curated-search
title: "Table User Picker: Search atas kolom curated saat Hidden dan setelah ditampilkan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-425
  - TC-AC-RP-428
  - TC-AC-RP-429
coverage:
  web: automated
---

# Table User Picker: Search atas kolom curated saat Hidden dan setelah ditampilkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Pool picker (Pre-setup #12): `Maya Putri` (Pending Activation), `Agus Salim` (akun sementara sampai 31 Des 2026, TAG `TAG-0001`), `Alex Tan` (Nickname `ALX`); `Agus Salim` belum memegang tingkat akses pada awal spec (kondisi baseline).
- State yang diubah: konfigurasi kolom picker disimpan di browser; antar blok dipulihkan dengan menghilangkan centang kolom (langkah penghubung) dan hook `after` menghapus preferensi kolom (kemampuan disediakan tim FE).

## Test Steps

1. Klik tombol "+ Assign"

### TC-AC-RP-425: Search picker mencakup kolom curated Activation Status, Temporary User, TAG setelah ditampilkan dan tidak mencakup saat Hidden

2. Ketik Search `Pending Activation`, tekan Enter
3. Verifikasi hasil "No results found" tampil (kolom Activation Status Hidden tidak tercakup Search)
4. Klik `(←)` pada kotak Search
5. Klik header kolom Actions pada picker, lalu pilih Column Visibility dan centang Activation Status, Temporary User, dan TAG
6. Ketik Search `Pending Activation`, tekan Enter
7. Verifikasi baris `Maya Putri` tampil (kolom Activation Status = `Pending Activation`)
8. Ganti isi kotak search dengan `tag-0001`, tekan Enter
9. Verifikasi baris `Agus Salim` tampil (kolom TAG)
10. Verifikasi tidak ada baris selain `Agus Salim`
11. Ganti isi kotak search dengan `Yes`, tekan Enter
12. Verifikasi baris `Agus Salim` tampil (kolom Temporary User = `Yes`)

### TC-AC-RP-428: Search picker mencakup kolom curated Custom Field aktif setelah ditampilkan dan tidak mencakup saat Hidden

13. Klik `(←)` pada kotak Search
14. Ketik Search `ALX`, tekan Enter
15. Verifikasi hasil "No results found" tampil (kolom `Nickname` Hidden tidak tercakup Search)
16. Klik `(←)` pada kotak Search
17. Klik header kolom Actions pada picker, lalu pilih Column Visibility dan centang `Nickname`
18. Ketik Search `ALX`, tekan Enter
19. Verifikasi baris `Alex Tan` tampil (kolom `Nickname` = `ALX`)
20. Verifikasi tidak ada baris selain `Alex Tan`

### TC-AC-RP-429: Search picker tidak mencakup kolom tanggal Temporary Until walau kolom ditampilkan

21. Klik `(←)` pada kotak Search
22. Hilangkan centang Activation Status, Temporary User, TAG, dan `Nickname` pada Column Visibility picker (pulihkan kolom bawaan)
23. Klik header kolom Actions pada picker, lalu pilih Column Visibility dan centang Temporary User dan Temporary Until
24. Ketik Search nilai yang tampil pada sel Temporary Until baris `Agus Salim` (`31 Des 2026`), tekan Enter
25. Verifikasi hasil "No results found" tampil (kolom tanggal Temporary Until tidak tercakup Search)
26. Klik `(←)` pada kotak Search
27. Ketik Search `Yes`, tekan Enter
28. Verifikasi baris `Agus Salim` tampil (kolom Temporary User = `Yes`)
29. Tutup popup Table User Picker dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Picker dibuka sekali di langkah 1 untuk seluruh TC (langkah membuka picker TC berikutnya tidak diulang; konvensi bagian 3).
- Langkah penghubung (tanpa awalan Verifikasi): langkah 4, 13, 16, 21, dan 26 mengosongkan Search lewat `(←)` (R-16); langkah 22 memulihkan kolom bawaan sebelum TC-AC-RP-429 yang mencentang Temporary User; langkah 29 menutup picker.
- Temuan untuk QA:
  - TC-AC-RP-429 menyebut nilai tanggal "31 Des 2026" sedangkan format tanggal default entitas uji pada Catatan TC memakai singkatan bulan Inggris (contoh "15 Jun 2026"); spec memakai nilai yang tampil pada sel baris `Agus Salim` seperti TC.
  - TC-AC-RP-425, 428, dan 429 tidak menyebut `[Save]` pada Column Visibility picker; spec mengikuti TC.
