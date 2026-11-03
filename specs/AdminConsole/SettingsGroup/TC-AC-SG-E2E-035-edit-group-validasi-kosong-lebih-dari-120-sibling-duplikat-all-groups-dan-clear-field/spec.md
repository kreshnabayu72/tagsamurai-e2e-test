---
id: TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field
title: "Edit Group: Validasi (Kosong, Lebih dari 120, Sibling Duplikat, All Groups, Clear Field)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-118
  - TC-AC-SG-119
  - TC-AC-SG-120
  - TC-AC-SG-122
  - TC-AC-SG-124
coverage:
  web: automated
---

# Edit Group: Validasi (Kosong, Lebih dari 120, Sibling Duplikat, All Groups, Clear Field)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: node Pre-setup `Region B` (level 1) dan `Branch 2` (anak `Region A`, sibling `Branch 1`) dari `Pohon Uji Utama` (Pre-setup #16) dibaca saja. Semua `[Save]` ditolak validasi atau tidak dilakukan, sehingga tidak ada data yang ditulis; nilai ketikan memakai nilai literal TC karena tidak pernah disimpan.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### Blok popup Edit `Region B`: TC-AC-SG-118, TC-AC-SG-119, TC-AC-SG-122

1. Ketik Search `Region B`, tekan Enter
2. Klik ikon `⋯` pada baris `Region B`, lalu pilih "Edit"

#### TC-AC-SG-118: Nama dikosongkan

3. Hapus seluruh isi Group Name
4. Klik `[Save]`
5. Verifikasi inline error: "Group name must not be empty"
6. Verifikasi popup tetap terbuka

#### TC-AC-SG-119: Lebih dari 120 karakter

7. Ketik nama 121 karakter "B" pada Group Name
8. Verifikasi error langsung muncul: "Max. 120 characters"

#### TC-AC-SG-122: Nama All Groups

9. Ganti isi Group Name dengan `all groups`
10. Klik `[Save]`
11. Verifikasi inline error: "'All Groups' is a reserved name and cannot be used"
12. Klik `[✕]` pada popup
13. Verifikasi dialog Unsaved Changes tampil
14. Klik `[Leave]`
15. Verifikasi nama baris `Region B` tidak berubah pada tabel

### Blok popup Edit `Branch 2`: TC-AC-SG-120

16. Ganti isi kotak search dengan `Branch 2`, tekan Enter
17. Klik ikon `⋯` pada baris `Branch 2`, lalu pilih "Edit"
18. Ganti isi Group Name dengan `branch 1` (sibling di bawah `Region A`), lalu berhenti mengetik sekitar 500 ms
19. Verifikasi error setelah jeda: "Group name already exists in this level"
20. Kembalikan nilai Group Name menjadi `Branch 2` persis
21. Verifikasi error hilang (diri sendiri dikecualikan dari pengecekan duplikat)
22. Klik `[✕]` pada popup

### Blok popup Edit `Region B`: TC-AC-SG-124

23. Ganti isi kotak search dengan `Region B`, tekan Enter
24. Klik ikon `⋯` pada baris `Region B`, lalu pilih "Edit"
25. Klik `[Clear Field]`
26. Verifikasi field Group Name kosong (bukan kembali ke "Region B")
27. Verifikasi popup tetap terbuka
28. Verifikasi tidak ada dialog konfirmasi
29. Klik `[✕]` pada popup
30. Verifikasi dialog Unsaved Changes tampil
31. Klik `[Leave]`
32. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Satu pembukaan popup dipakai untuk TC-AC-SG-118, 119, dan 122 karena semuanya hanya mengetik atau ditolak validasi tanpa Save sukses (bagian 3 prinsip 13, halaman yang sama dipakai berulang); TC-AC-SG-124 memakai pembukaan baru karena Expected-nya bergantung pada nilai awal `Region B` yang terisi.
- Langkah penghubung (S-03): langkah 1, 16, dan 23 (Search untuk menemukan baris target, R-16), langkah 22 (menutup popup yang nilainya sudah dikembalikan sama dengan nilai tersimpan; tertutup tanpa dialog, lihat TC-AC-SG-126 di spec 037), langkah 32 (reset Search, S-09).
- Langkah 15 memakai langkah 5, 8, dan 11 (error tampil dan dialog) sebagai bukti respons yang diproses; nama baris pada tabel yang tidak berubah adalah asersi "data tidak berubah" TC-AC-SG-118 dan TC-AC-SG-122.
- Temuan untuk QA: TC-AC-SG-120 tidak menyebut apakah popup tertutup tanpa dialog setelah nilai dikembalikan ke nilai tersimpan; langkah 22 tidak mengasersinya (dicakup TC-AC-SG-126).
