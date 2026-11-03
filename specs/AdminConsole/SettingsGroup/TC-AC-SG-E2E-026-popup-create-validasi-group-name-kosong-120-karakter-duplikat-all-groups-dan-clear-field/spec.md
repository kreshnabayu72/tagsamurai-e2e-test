---
id: TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field
title: "Popup Create: Validasi Group Name (Kosong, 120 Karakter, Duplikat, All Groups, Clear Field)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-81
  - TC-AC-SG-82
  - TC-AC-SG-84
  - TC-AC-SG-87
  - TC-AC-SG-88
coverage:
  web: automated
---

# Popup Create: Validasi Group Name (Kosong, 120 Karakter, Duplikat, All Groups, Clear Field)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja; `Region A` (level 1) menjadi sibling pembanding untuk validasi duplikat. Semua submit pada spec ini ditolak validasi atau tidak dilakukan, sehingga tidak ada data yang ditulis. Nilai ketikan memakai nilai literal TC karena tidak pernah disimpan.
- Jumlah group dasar (N) dibaca dari label root "All Groups (N)" sebelum aksi pertama; tidak memakai angka absolut.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

1. Catat jumlah group N pada label root "All Groups (N)" di Sidebar Group Tree
2. Klik `[+] Group` di Sidebar Group Tree

### TC-AC-SG-81: Group Name kosong setelah Submit

3. Klik `[Submit]` tanpa mengisi Group Name
4. Verifikasi inline error di bawah field: "Group name must not be empty"
5. Verifikasi popup tetap terbuka
6. Verifikasi label root tetap "All Groups (N)" (tidak ada group baru)

### TC-AC-SG-82: Batas panjang 120 karakter

7. Ketik 120 karakter "A" pada Group Name
8. Verifikasi tidak ada error pada Group Name
9. Verifikasi `[Submit]` dapat dipakai
10. Ketik 1 karakter tambahan (121 karakter) pada Group Name
11. Verifikasi error langsung muncul tanpa menunggu Submit: "Max. 120 characters"
12. Klik `[Clear Field]`

### TC-AC-SG-84: Nama duplikat pada parent yang sama

13. Ketik `region a` pada Group Name (huruf kecil, sama dengan sibling level 1 `Region A`), lalu berhenti mengetik selama sekitar 500 ms tanpa berpindah fokus
14. Verifikasi inline error muncul setelah jeda sekitar 500 ms (bukan menunggu blur): "Group name already exists in this level"
15. Klik `[Submit]`
16. Verifikasi label root tetap "All Groups (N)" (`[Submit]` tidak membuat group baru)
17. Klik `[Clear Field]`

### TC-AC-SG-87: Nama All Groups direservasi

18. Ketik `ALL GROUPS` pada Group Name, klik `[Submit]`
19. Verifikasi inline error: "'All Groups' is a reserved name and cannot be used"
20. Ganti isi Group Name dengan `all groups`, klik `[Submit]`
21. Verifikasi inline error: "'All Groups' is a reserved name and cannot be used"
22. Ganti isi Group Name dengan `All Groups`, klik `[Submit]`
23. Verifikasi inline error: "'All Groups' is a reserved name and cannot be used"
24. Verifikasi label root tetap "All Groups (N)" (tidak ada group dibuat oleh ketiga varian)
25. Klik `[Clear Field]`

### TC-AC-SG-88: Tombol Clear Field

26. Centang "Stay on this form after submitting"
27. Ketik `Region A` pada Group Name hingga error duplikat muncul
28. Klik `[Clear Field]`
29. Verifikasi field Group Name kosong
30. Verifikasi border dan pesan error hilang
31. Verifikasi fokus kembali ke field Group Name
32. Verifikasi popup tetap terbuka tanpa dialog konfirmasi
33. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
34. Hilangkan centang "Stay on this form after submitting", lalu klik `[✕]` pada popup

## Notes

- Langkah penghubung (S-03): langkah 1 (mencatat N sebagai baseline hitungan group), langkah 12, 17, dan 25 (`[Clear Field]` agar field tidak membawa error ke TC berikutnya, S-09), dan langkah 34 (mengembalikan checkbox dan menutup popup yang sudah kosong tanpa dialog Unsaved Changes).
- TC-AC-SG-84 Expected butir a "pengecekan tidak sensitif huruf besar/kecil" tampak dari nilai uji `region a` yang cocok dengan `Region A` (langkah 14) dan tidak diasersi terpisah.
- Satu pembukaan popup dipakai untuk kelima TC karena semuanya hanya mengetik atau ditolak validasi tanpa submit sukses (bagian 3 prinsip 13, halaman yang sama dipakai berulang).
