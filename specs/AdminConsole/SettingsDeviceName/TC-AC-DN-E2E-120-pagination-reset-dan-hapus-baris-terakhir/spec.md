---
id: TC-AC-DN-E2E-120-pagination-reset-dan-hapus-baris-terakhir
title: "Pagination List: Nomor Tidak Valid, Reset Halaman, 130 Baris, dan Hapus Baris Terakhir"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-360
  - TC-AC-DN-361
  - TC-AC-DN-362
  - TC-AC-DN-363
  - TC-AC-DN-364
coverage:
  web: automated
---

# Pagination List: Nomor Tidak Valid, Reset Halaman, 130 Baris, dan Hapus Baris Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti, #17 seed `Seed Device 001` sampai `Seed Device 120`, dan #23 nama panjang `Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan`; total 130 baris (TC-AC-DN-360 sampai TC-AC-DN-363).
- Data Dinamis (milik spec, TC-AC-DN-364): 21 Device Name `Hapus Halaman {runId}-120 01` sampai `Hapus Halaman {runId}-120 21` (Measurement `Unit`, Category `Accessory`, tanpa SKU), dibuat lewat API pada langkah 27 sesudah TC-AC-DN-360 sampai TC-AC-DN-363 selesai, agar 21 record tidak menggeser isi halaman 130 baris (kemampuan seeding disediakan tim FE/BE); hook `after` menghapus record yang masih ada sebagai cadangan pembersihan. `{runId}` hanya digit. Satu record (`... 21`) dihapus oleh aksi Delete di UI; 20 record lainnya dihapus lewat API pada langkah 36.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah selain record milik spec. Page size dan halaman dikembalikan ke 10 dan halaman 1 di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-360: Nomor halaman tidak valid diabaikan

1. Ketik `2` pada input nomor halaman, tekan Enter
2. Ketik `0` pada input nomor halaman, tekan Enter
3. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2 (Seed Device 003 sampai Seed Device 012)
4. Ketik `999` pada input nomor halaman, tekan Enter
5. Verifikasi input `999` diabaikan dan tabel tetap di halaman 2 (Seed Device 003 sampai Seed Device 012)
6. Ketik `-1` pada input nomor halaman, tekan Enter
7. Verifikasi input `-1` diabaikan dan tabel tetap di halaman 2 (Seed Device 003 sampai Seed Device 012)
8. Ketik `abc` pada input nomor halaman, tekan Enter
9. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2 (Seed Device 003 sampai Seed Device 012)

### TC-AC-DN-361: Mengganti page size kembali ke halaman 1

10. Ketik `1` pada input nomor halaman, tekan Enter
11. Klik tombol halaman berikutnya dua kali
12. Pilih page size `25`
13. Verifikasi tabel kembali ke halaman 1 dengan 25 baris

### TC-AC-DN-362: Mengganti sort tetap di nomor halaman yang sama

14. Pilih page size `10`
15. Klik tombol halaman berikutnya
16. Klik header `Device Name` dua kali (descending)
17. Verifikasi tabel tetap di halaman 2 (nomor halaman tidak berubah)
18. Verifikasi urutan descending: halaman 2 dimulai Seed Device 112
19. Klik header `Device Name` ketiga kali (netral)
20. Ketik `1` pada input nomor halaman, tekan Enter

### TC-AC-DN-363: Dua halaman penuh pada page size 100 untuk 130 baris

21. Pilih page size `100`
22. Klik tombol halaman berikutnya
23. Verifikasi halaman 2 menampilkan 30 baris
24. Verifikasi halaman 2 berakhir pada `Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan`
25. Verifikasi tombol halaman berikutnya tidak aktif di halaman 2
26. Pilih page size `10`
27. Buat 21 Device Name `Hapus Halaman {runId}-120 01` sampai `Hapus Halaman {runId}-120 21` (Measurement `Unit`, Category `Accessory`, tanpa SKU) lewat API hingga tersimpan

### TC-AC-DN-364: Menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang masih ada

28. Ketik Search `Hapus Halaman {runId}-120`, tekan Enter
29. Klik tombol halaman berikutnya dua kali
30. Buka menu aksi pada baris `Hapus Halaman {runId}-120 21`, klik `Delete`
31. Klik `[Delete]` pada dialog konfirmasi `Delete Device Name`
32. Verifikasi toast sukses: "Success, device name has been deleted."
33. Verifikasi tabel pindah ke halaman 2 (halaman terakhir yang masih ada)
34. Verifikasi halaman 2 menampilkan 10 baris: `Hapus Halaman {runId}-120 11` sampai `Hapus Halaman {runId}-120 20`
35. Klik `(←)` pada kotak Search
36. Hapus 20 Device Name `Hapus Halaman {runId}-120 01` sampai `20` lewat API hingga terhapus

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09, R-16): langkah 10, 14, 19 sampai 20, 26, dan 35 mengembalikan halaman, page size, sort, dan Search ke awal; langkah 27 membuat 21 record milik spec lewat API di tengah spec (bukan di hook `before`) supaya data TC-AC-DN-360 sampai TC-AC-DN-363 tetap 130 baris; langkah 28 (Search `Hapus Halaman {runId}-120`) menyaring ke 21 record milik spec sehingga halaman 3 berisi tepat satu baris; langkah 36 membersihkan record milik spec (hook `after` sebagai cadangan).
- Record milik spec (S-06, S-12): TC sumber menghapus `Seed Device 120` (Pre-setup #17) dengan Search `Seed Device 1` (21 baris); spec memakai 21 record milik spec bersuffix `{runId}-120` yang menghasilkan struktur halaman yang sama (3 halaman, halaman 3 berisi 1 baris) sehingga seed 120 baris baca-saja tidak dihapus dan tidak perlu dipulihkan. Halaman 2 setelah hapus berisi 10 baris `... 11` sampai `... 20`, bukan `Seed Device 110` sampai `119`.
- Ukuran spec (36 langkah, di atas smell 35 langkah): satu topik (pagination List), satu dataset; tiap blok mengembalikan halaman, page size, dan sort ke awal sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc; aksi menghapus data (TC-AC-DN-364) di akhir.
- Temuan untuk QA:
  - TC-AC-DN-360 Expected untuk empat masukan ditulis satu `Verifikasi` per masukan (langkah 3, 5, 7, 9).
  - TC-AC-DN-364 Post Condition ("Device Name `Seed Device 120` terhapus (dipulihkan automation baseline)") tanpa langkah observasi tidak diasersi.
