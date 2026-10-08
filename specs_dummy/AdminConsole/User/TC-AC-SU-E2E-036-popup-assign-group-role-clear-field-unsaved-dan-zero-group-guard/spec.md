---
id: TC-AC-SU-E2E-036-popup-assign-group-role-clear-field-unsaved-dan-zero-group-guard
title: "Assign Group Role: Siklus Clear Field, Guard Unsaved Changes, dan Dialog Blokir 0 Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-79
  - TC-AC-SU-99
  - TC-AC-SU-101
  - TC-AC-SU-251
  - TC-AC-SU-259
coverage:
  web: automated
---

# Assign Group Role: Siklus Clear Field, Guard Unsaved Changes, dan Dialog Blokir 0 Group

## Prerequisites

- Login sebagai Total Control
- Modal Assign Group Role sedang terbuka dengan data terisi

## Test Steps

### Interaksi Reset via [Clear Field]
1. Pada modal Assign Group Role, ubah pilihan grup atau tambahkan baris baru
2. Klik tombol `[Clear Field]` pada bagian footer kiri modal
3. Verifikasi seluruh perubahan input dibersihkan dan form kembali ke state awal sebelum diedit

### Guard Unsaved Changes Dialog
4. Lakukan penambahan 1 grup baru sehingga form berada pada status kotor (dirty)
5. Klik tombol silang `✕`, tombol `[Cancel]`, atau tekan tombol keyboard `Esc`
6. Verifikasi dialog konfirmasi Unsaved Changes muncul: `"You have unsaved changes. Are you sure you want to leave?"`
7. Klik tombol `[Stay]`; verifikasi dialog tertutup dan input modal tetap utuh
8. Klik tombol silang `✕` kembali lalu klik `[Leave]`
9. Verifikasi modal tertutup dan perubahan kotor dibatalkan

### Guard Pemblokiran Submit 0 Group
10. Buka kembali modal Assign Group Role dan hapus seluruh grup yang terdaftar hingga tersisa 0 grup
11. Klik tombol `[Save]`
12. Verifikasi sistem memblokir submit dan menampilkan dialog pencegahan: `"At least one group must be assigned. To remove all access, please toggle off the role instead."`

## Notes

Menjaga konsistensi data form dan mencegah penugasan peran tanpa grup anggota.
