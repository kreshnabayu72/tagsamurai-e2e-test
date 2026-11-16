---
id: TC-FA-FACO-UI-121-tabel-state-data
title: "Tab Chart of Accounts: loading, kosong, kosong tersaring, dan gagal muat"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ST-11, ST-12, ST-13, ST-16, "§7.1#p1", "EB-TBL-1@tabel-account-list"]
smoke: []
dependsOn: []
trace:
  ST-11: [2, 4, 18]
  ST-12: 2
  ST-13: [18, 19]
  ST-16: [4, 5, 12, 15, 16]
  "§7.1#p1": [6, 7]
  "EB-TBL-1@tabel-account-list": [4, 15, 18, 20]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: loading, kosong, kosong tersaring, dan gagal muat

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-121-1: Account `5-6001`, Name `Depreciation Expense – Admin`, Function `Depreciation Expense`, status Active, Used By `0`, Last Used in Journal kosong, satu-satunya akun pada daftar.
  - DU-121-2: daftar akun kosong, jumlah akun `0`.
  - DU-121-3: Account `1-1001`, Name `Fixed Assets – Equipment`, Function `Asset Cost`, status Active, Used By `3`, Last Used in Journal `Oct 2026`.
  - DU-121-4: kata kunci Search `Zxqv Tidak Ada`, tidak cocok dengan akun mana pun.
- Kondisi:
  - K1: memuat daftar sedang berlangsung dan belum dijawab.
  - K2: daftar kosong menurut DU-121-2.
  - K3: daftar berisi DU-121-1 saja; penghapusan DU-121-1 berhasil dan daftar berikutnya kosong.
  - K4: daftar berisi DU-121-3; kata kunci Search `Zxqv Tidak Ada` menghasilkan daftar kosong.
  - K5: memuat daftar gagal karena error server.

## Test Steps

### Tabel sedang memuat
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Verifikasi tabel menandai keadaan memuat dan belum menampilkan baris akun

### Daftar kosong
3. Tampilkan Tab Chart of Accounts dengan kondisi K2
4. Verifikasi judul `No account yet` tampil
5. Verifikasi deskripsi `Get started by creating your first account.` tampil
6. Verifikasi tombol `[+ Account]` di toolbar tampil
7. Verifikasi empty state tidak memuat tombol aksi

### Daftar menjadi kosong setelah akun terakhir dihapus
8. Tampilkan Tab Chart of Accounts dengan kondisi K3
9. Klik `⋯` pada baris `5-6001`
10. Klik `Delete`
11. Klik `[Delete]` pada dialog `Delete Account`
12. Verifikasi judul `No account yet` tampil

### Daftar kosong karena Search
13. Tampilkan Tab Chart of Accounts dengan kondisi K4
14. Ketik Search `Zxqv Tidak Ada`, tekan Enter
15. Verifikasi judul `No results found` tampil
16. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Gagal memuat daftar
17. Tampilkan Tab Chart of Accounts dengan kondisi K5
18. Verifikasi pesan `Unable to load this data.` tampil
19. Verifikasi tombol `[Try Again]` tampil
20. Verifikasi judul `No account yet` tidak tampil
