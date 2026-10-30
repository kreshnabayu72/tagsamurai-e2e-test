---
id: TC-GS-DIV-E2E-039-bulk-delete-blokir-seluruhnya-atau-satu-in-use
title: "Bulk Delete Diblokir: Seluruhnya In-Use dan Satu Baris In-Use"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-136
  - TC-GS-DIV-138
coverage:
  web: automated
---

# Bulk Delete Diblokir: Seluruhnya In-Use dan Satu Baris In-Use

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah atau menghapus data; kedua kasus berakhir dengan dialog blokir.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (data environment tetap, tidak diubah atau dihapus spec ini; nama literal tanpa suffix karena tidak dibuat atau diubah): `Human Resources` (HR, in-use Login User aktif Budi Santoso), `Operations` (OPS, in-use Login User non-aktif Siti Rahmawati), dan `Compliance` (CMP, in-use Non-Login User Andi Pratama). Fixture belum ada; tim FE menyiapkan kunci `humanResources`, `operations`, dan `compliance` pada fixture Division. Bulk Delete pada ketiganya diblokir (no-op): data dan Last Updated tidak berubah.
- Opsi page size 50 tersedia pada paginasi tabel, supaya ketiga Division Pre-setup berada pada halaman yang sama dengan Division lain milik spec lain yang mungkin ada.
- Data dinamis: tidak ada; tidak ada seeding dan tidak ada cleanup selain memulihkan page size (10) dan membersihkan seleksi. Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan

1. Ubah page size tabel menjadi 50

### TC-GS-DIV-136: Bulk Delete seluruhnya in-use menampilkan Dialog blokir dengan bullet diperluas

2. Centang baris `Human Resources`
3. Centang baris `Operations`
4. Klik `Bulk Action` > `Delete`
5. Verifikasi tidak ada toast sukses
6. Verifikasi dialog `Cannot Delete Data` tampil
7. Verifikasi dialog `Delete Division` tidak tampil (bukan dialog dengan kelompok kosong)
8. Verifikasi Body memuat bullet `Human Resources` dan `Operations`
9. Verifikasi Body memuat teks `These divisions are still in use. Remove the references before deleting.`
10. Verifikasi dialog hanya punya satu tombol `[OK]`
11. Klik `[OK]`
12. Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-138: Bulk Delete dengan satu baris in-use memakai dialog blokir single

13. Centang baris `Compliance`
14. Klik `Bulk Action` > `Delete`
15. Verifikasi dialog `Cannot Delete Data` tampil dalam bentuk single dengan bullet `Compliance`
16. Verifikasi Body memuat teks `This division is still in use. Remove the references before deleting.`
17. Verifikasi dialog hanya punya satu tombol `[OK]`
18. Klik `[OK]`
19. Klik icon `(✕)` pada Bulk Action Bar
20. Ubah page size tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Kelas harness: blokir kondisi data, bagian 3 prinsip 12.
- Subjudul `###` memetakan langkah ke id TC. Urutan mengikuti sourceTc; tidak ada aksi yang menghapus data di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (page size 50), 11 dan 18 (klik `[OK]` untuk menutup dialog yang di TC sumber tidak ditutup), 12 dan 19 (membersihkan seleksi), 20 (memulihkan page size).
- Bentuk "single" pada TC-138 butir a dipecah menjadi bullet `Compliance` (langkah 15) dan teks singular (langkah 16).
- Temuan untuk QA:
  - TC-136 butir c ("tidak ada toast sukses") dan TC-138 tidak menyebut toast item dilewati; spec hanya mengasersi yang tertulis.
  - TC-136 dan TC-138 Post Condition ("Kedua Division tetap ada") tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-136 dan TC-138 tidak menyebut cara menampilkan baris pada halaman yang sama; spec memakai page size 50.
