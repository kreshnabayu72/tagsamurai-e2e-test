---
id: TC-GS-ACTLOG-E2E-022-tab-session-populate-opsi-filter-dari-data-log
title: "Tab Session: Opsi Filter Terpopulasi Dinamis dari Data Tabel dan Ketiadaan Opsi None"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-78
  - TC-GS-ACTLOG-79
  - TC-GS-ACTLOG-80
  - TC-GS-ACTLOG-113
  - TC-GS-ACTLOG-114
  - TC-GS-ACTLOG-115
coverage:
  web: automated
---

# Tab Session: Opsi Filter Terpopulasi Dinamis dari Data Tabel dan Ketiadaan Opsi None

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Entitas uji dengan data log terbatas

## Test Steps

### Opsi Dinamis Bersumber dari Data
1. Buka Tab Session, buka Filter Panel.
2. Buka daftar opsi pada field User, Position, Division, Activity, Status.
3. Verifikasi daftar opsi hanya memuat nilai yang genuinely ada pada data baris tabel saat ini.
4. Verifikasi tidak ada opsi bernilai 'None', '—', atau opsi string kosong pada seluruh field.
### Penambahan Opsi Realtime & Retensi Data Dihapus
5. Lakukan login pengguna baru 'Siti Nurbaya' di sesi browser lain.
6. Tanpa refresh halaman, buka kembali dropdown field User di Tab Session.
7. Verifikasi nama 'Siti Nurbaya' otomatis muncul di daftar opsi.
8. Filter User 'Budi Anwar', lalu hapus akun 'Budi Anwar' di master user.
9. Muat ulang Tab Session dengan filter aktif, verifikasi opsi 'Budi Anwar' dan datanya tetap bertahan di riwayat log.
### Loading State & Empty Options
10. Buka dropdown filter saat koneksi lambat, verifikasi indikator spinner/skeleton mini tampil di dropdown.
11. Intercept data log menjadi 0 baris, buka dropdown filter, verifikasi menampilkan teks 'No options available' tanpa error.

## Notes

- Opsi filter tidak memakai enum statis melainkan terpopulasi dinamis dari dataset aktual.
