---
id: TC-FA-CAID-E2E-039-pencatatan-log-edit-segments-formula-dan-initial-company
title: "Pencatatan Log Edit: Segments Formula Dicentang dan Perubahan Initial Company"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-239
  - TC-FA-CAID-240
  - TC-FA-CAID-241
  - TC-FA-CAID-242
coverage:
  web: automated
---

# Pencatatan Log Edit: Segments Formula Dicentang dan Perubahan Initial Company

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) untuk TC-FA-CAID-239 dan TC-FA-CAID-240 dan baseline B2 (No 10: Separator Dash, Initial Company `ABC`, Division Code tercentang) untuk TC-FA-CAID-241 dan TC-FA-CAID-242. Baseline B1 dan B2 disiapkan lewat seed API pada langkah pertama tiap TC. General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: konfigurasi Company Alpha berubah di tiap TC. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-239: Log Edit Segments Formula untuk segmen yang dicentang

1. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
2. Centang `Division Code`
3. Klik `[Save]`
4. Tunggu aksi selesai: tombol `[Save]` kembali disabled
5. Buka Modal Changelog: Custom Asset ID
6. Verifikasi tepat satu baris baru dibanding baseline dengan Action `Edit`, Field `Segments Formula`, Old Value `—`, New Value `(Division Code) Inactive ➔ Active`
7. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
8. Verifikasi baris yang sama muncul di System Log dengan Object `Custom Asset ID` dan Name `—`
9. Buka Fixed Asset > Activity Log > tab User Action
10. Verifikasi baris yang sama muncul di Activity Log dengan Modified By `Sarah J`
11. Verifikasi kolom Old Value baris ini berisi `—` dan seluruh delta berada di New Value, sama di ketiga surface

### TC-FA-CAID-240: Log Edit saat Initial Company dicentang dan diisi

12. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
13. Centang `Initial Company` dan ketik `ABC`
14. Klik `[Save]`
15. Tunggu aksi selesai: tombol `[Save]` kembali disabled
16. Buka Modal Changelog: Custom Asset ID
17. Verifikasi satu baris baru dibanding baseline Action `Edit`, Field `Segments Formula`, Old Value `—`, New Value `(Initial Company) Inactive ➔ Active; (Initial Company) '—' ➔ 'ABC'` tampil di Changelog
18. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
19. Verifikasi satu baris baru yang sama tampil di System Log
20. Buka Fixed Asset > Activity Log > tab User Action
21. Verifikasi satu baris baru yang sama tampil di Activity Log
22. Verifikasi kolom Old Value baris ini berisi `—` dan seluruh delta berada di New Value, sama di ketiga surface

### TC-FA-CAID-241: Log Edit saat Initial Company di-uncheck dari kondisi Active bernilai ABC

23. Atur konfigurasi Company Alpha ke baseline B2 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
24. Hilangkan centang `Initial Company`
25. Klik `[Save]`
26. Tunggu aksi selesai: tombol `[Save]` kembali disabled
27. Buka Modal Changelog: Custom Asset ID
28. Verifikasi satu baris baru dibanding baseline Action `Edit`, Field `Segments Formula`, Old Value `—`, New Value `(Initial Company) Active ➔ Inactive; (Initial Company) 'ABC' ➔ '—'` tampil di Changelog
29. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
30. Verifikasi satu baris baru yang sama tampil di System Log
31. Buka Fixed Asset > Activity Log > tab User Action
32. Verifikasi satu baris baru yang sama tampil di Activity Log
33. Verifikasi kolom Old Value baris ini berisi `—` dan seluruh delta berada di New Value, sama di ketiga surface

### TC-FA-CAID-242: Log Edit saat nilai Initial Company berubah dari ABC ke XYZ

34. Atur konfigurasi Company Alpha ke baseline B2 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
35. Ubah isi input Initial Company menjadi `XYZ`
36. Klik `[Save]`
37. Tunggu aksi selesai: tombol `[Save]` kembali disabled
38. Buka Modal Changelog: Custom Asset ID
39. Verifikasi satu baris baru dibanding baseline Action `Edit`, Field `Segments Formula`, Old Value `—`, New Value `(Initial Company) 'ABC' ➔ 'XYZ'` tampil di Changelog
40. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
41. Verifikasi satu baris baru yang sama tampil di System Log
42. Buka Fixed Asset > Activity Log > tab User Action
43. Verifikasi satu baris baru yang sama tampil di Activity Log
44. Verifikasi kolom Old Value baris ini berisi `—` dan seluruh delta berada di New Value, sama di ketiga surface

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 44 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik dan satu kelas harness (pencatatan log Edit Segments Formula) dengan empat blok TC yang berpola sama; blok baca-log berpola (buka surface, lalu `Verifikasi` kolom log) tidak dihitung menurut bagian 3 prinsip 13, sehingga langkah di luar blok itu hanya 16 (langkah 1 sampai 4, 12 sampai 15, 23 sampai 26, dan 34 sampai 37).
- Langkah penghubung: langkah 1, 12, 23, dan 34 (seed baseline, membuka halaman, dan baseline jumlah entri, S-12), langkah 4, 15, 26, dan 37 (tunggu aksi selesai sebelum membuka Modal Changelog, bagian 8b butir 8), serta membuka Modal Changelog, System Log, dan Activity Log.
- Ketiga surface diasersi per surface (Changelog, System Log, Activity Log) sebelum `Verifikasi` Old Value/New Value yang "sama di ketiga surface" pada langkah 11, 22, 33, dan 44.
- Pembagian TC lintas spec: TC-FA-CAID-233 sampai 235 ada di spec 037, TC-FA-CAID-236 sampai 238 di spec 038, TC-FA-CAID-243 sampai 245 di spec 040.
- Temuan untuk QA:
  - TC-FA-CAID-239 Expected b tidak menyebut Field/Old/New untuk baris System Log dan Activity Log secara terpisah; spec mengasersinya sama dengan Changelog sesuai Expected c ("sama di ketiga surface").
  - Post Condition TC-FA-CAID-239 sampai 242 tidak diasersi karena TC tidak memberi langkah observasinya.
