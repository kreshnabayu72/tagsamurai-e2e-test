---
id: TC-GS-DIV-E2E-032-delete-single-blokir-in-use
title: "Delete Division Single: Diblokir karena In-Use (Login Aktif, Non-Aktif, Non-Login User)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-117
  - TC-GS-DIV-118
  - TC-GS-DIV-119
  - TC-GS-DIV-120
coverage:
  web: automated
---

# Delete Division Single: Diblokir karena In-Use (Login Aktif, Non-Aktif, Non-Login User)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah atau menghapus data; semua kasus berakhir tanpa penghapusan.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (data environment tetap, tidak diubah atau dihapus spec ini; nama literal tanpa suffix karena tidak dibuat atau diubah): `Human Resources` (HR, in-use Login User aktif Budi Santoso), `Operations` (OPS, in-use Login User non-aktif Siti Rahmawati), dan `Compliance` (CMP, in-use Non-Login User Andi Pratama). Fixture belum ada; tim FE menyiapkan kunci `humanResources`, `operations`, dan `compliance` pada fixture Division. Aksi Delete pada ketiganya diblokir (no-op): data dan Last Updated tidak berubah.
- Data dinamis: tidak ada; tidak ada seeding dan tidak ada cleanup selain mengosongkan Search. Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-117: Delete Division yang dipakai Login User aktif diblokir

1. Ketik Search `Human Resources`, tekan Enter
2. Buka row action baris `Human Resources` lalu klik `Delete`
3. Verifikasi tidak ada toast
4. Verifikasi dialog konfirmasi hapus `Delete Division` tidak tampil
5. Verifikasi dialog `Cannot Delete Data` langsung tampil
6. Verifikasi severity dialog `Cannot Delete Data` adalah warning
7. Verifikasi Body memuat bullet `Human Resources`
8. Verifikasi Body memuat teks `This division is still in use. Remove the references before deleting.`
9. Verifikasi dialog hanya punya satu tombol `[OK]` (Single Dismiss Rule)

### TC-GS-DIV-120: OK pada dialog blokir menutup dialog tanpa menghapus

10. Klik `[OK]`
11. Verifikasi dialog `Cannot Delete Data` tertutup
12. Verifikasi baris `Human Resources` tetap ada

### TC-GS-DIV-118: Delete Division yang dipakai Login User non-aktif diblokir

13. Ganti isi kotak search dengan `Operations`, tekan Enter
14. Buka row action baris `Operations` lalu klik `Delete`
15. Verifikasi tidak ada toast
16. Verifikasi dialog konfirmasi hapus `Delete Division` tidak tampil
17. Verifikasi dialog `Cannot Delete Data` langsung tampil
18. Verifikasi severity dialog `Cannot Delete Data` adalah warning
19. Verifikasi Body memuat bullet `Operations`
20. Verifikasi Body memuat teks `This division is still in use. Remove the references before deleting.`
21. Verifikasi dialog hanya punya satu tombol `[OK]` (Single Dismiss Rule)
22. Klik `[OK]`

### TC-GS-DIV-119: Delete Division yang dipakai Non-Login User diblokir

23. Ganti isi kotak search dengan `Compliance`, tekan Enter
24. Buka row action baris `Compliance` lalu klik `Delete`
25. Verifikasi tidak ada toast
26. Verifikasi dialog konfirmasi hapus `Delete Division` tidak tampil
27. Verifikasi dialog `Cannot Delete Data` langsung tampil
28. Verifikasi severity dialog `Cannot Delete Data` adalah warning
29. Verifikasi Body memuat bullet `Compliance`
30. Verifikasi Body memuat teks `This division is still in use. Remove the references before deleting.`
31. Verifikasi dialog hanya punya satu tombol `[OK]` (Single Dismiss Rule)
32. Klik `[OK]`
33. Kosongkan isi kotak search lewat `(✕)`, tekan Enter

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC. Urutan di spec berbeda dari urutan sourceTc: TC-120 (klik `[OK]`) ditaruh langsung sesudah TC-117 karena memakai dialog yang sama (langkah "Buka row action ... lalu klik `Delete`" TC-120 sumber digabung ke langkah 2). Tidak ada aksi yang menghapus data di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1, 13, dan 23 (Search supaya baris Pre-setup tampil), 22 dan 32 (klik `[OK]` untuk menutup dialog yang di TC sumber tidak ditutup), 33 (membersihkan Search).
- Division Pre-setup tidak diberi suffix `{runId}` karena tidak dibuat, diubah, atau dihapus; kondisi in-use-nya adalah bagian dari data Pre-setup.
- Temuan untuk QA:
  - TC-117, TC-118, dan TC-119 Post Condition ("Division tidak terhapus") tidak punya langkah observasi di TC dan tidak diasersi (hanya TC-120 butir b yang mengasersi baris `Human Resources` tetap ada).
  - TC-117 sampai TC-119 tidak menyebut cara menemukan baris (Search, pagination, atau page size); spec memakai Search.
