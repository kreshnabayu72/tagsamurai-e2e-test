---
id: TC-GS-ACTLOG-E2E-018-tab-session-snapshot-immutability-data-historis-user
title: "Snapshot Immutability Tab Session: Data Historis Tidak Berubah Saat User Dimutasi atau Dihapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-54
  - TC-GS-ACTLOG-55
coverage:
  web: automated
---

# Snapshot Immutability Tab Session: Data Historis Tidak Berubah Saat User Dimutasi atau Dihapus

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat entri log lama milik user 'John Doe' (EMP001, Staff, Marketing) dan 'Budi Anwar' (EMP002, Supervisor, Finance)

## Test Steps

### Mutasi Profil Pengguna
1. Buka Global Settings > User, lakukan edit pada profil 'John Doe':
   - Ubah First Name menjadi 'Johnny'
   - Ubah Employee ID menjadi 'EMP101'
   - Ubah Position menjadi 'Manager'
   - Ubah Division menjadi 'Finance'
   - Klik [Save].
2. Buka Global Settings > Activity Log > Session.
3. Cari baris event masa lalu milik 'John Doe'.
4. Verifikasi nilai pada baris lama tetap membeku: User tetap 'John D' (hover 'John Doe'), Employee ID tetap 'EMP001', Position tetap 'Staff', Division tetap 'Marketing'.
### Penghapusan Akun Pengguna
5. Buka Global Settings > User, hapus akun pengguna 'Budi Anwar'.
6. Buka kembali Global Settings > Activity Log > Session.
7. Cari entri log masa lalu milik 'Budi Anwar'.
8. Verifikasi baris log tetap tampil utuh dengan User 'Budi A', Employee ID 'EMP002', Position 'Supervisor', Division 'Finance'.

## Notes

- Snapshot data pengguna dibekukan pada saat event terjadi untuk menjamin integritas forensik audit trail.
