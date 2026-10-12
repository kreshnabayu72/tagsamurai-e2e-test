---
id: TC-GS-BRAND-E2E-023-delete-blokir-in-use-client-dan-principal
title: "Delete Brand Diblokir karena In-Use pada Client dan Principal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-96
  - TC-GS-BRAND-97
  - TC-GS-BRAND-100
  - TC-GS-BRAND-99
  - TC-GS-BRAND-101
coverage:
  web: automated
---

# Delete Brand Diblokir karena In-Use pada Client dan Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`; relevan karena spec berakhir di akun Principal).
- Akun aktor 2: Total Control Principal (Hendra Wijaya) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, instance Principal. Login lewat langkah ganti akun eksplisit di tengah spec.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data pre-setup Client A (data environment tetap): `Acme Corp` (FAMS Asset Name: Forklift, 1 asset name) dan `Vertex Labs` (FAMS: 2 asset name, yaitu Laptop dengan 5 Model dan Monitor dengan Model `Vertex Ultra Long Model 000001`; Supply: 3 item type, yaitu Printer Ink, Scanner Paper, Toner Cartridge).
- Data pre-setup Principal (data environment tetap): `Signal One` (3 Device SKU: SKU-HR-001, SKU-TB-002, SKU-GW-003), `Relic Co` (1 Device SKU), `Ghost Co` (hanya dipakai Asset Name FAMS yang ada di Recycle Bin). Fixture belum ada; tim FE menyiapkan `fixtures/brand.json` (kunci `acmeCorp`, `vertexLabs`, `signalOne`, `relicCo`, `ghostCo`) dan akun Principal.
- Data dinamis: tidak ada. Semua kasus berakhir tanpa menghapus brand, sehingga tidak ada cleanup. Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > Master Reference > Brand.
- Kemampuan teknis: login ke dua instance (Client A lalu Principal) dalam satu spec dengan logout atau konteks browser bersih di antaranya.
- State global yang diubah: tidak ada.

## Test Steps

### Client A: Total Control (Sari Dewi)

1. Buka Global Settings > Master Reference > Brand

### TC-GS-BRAND-96: Delete Brand in-use menampilkan dialog blokir dengan breakdown Acme Corp

2. Cari baris Acme Corp (lewat pagination atau Search), lalu klik `⋯` > Delete
3. Verifikasi dialog blokir `Cannot Delete Brand` (warning) tampil
4. Verifikasi Body memuat `• Acme Corp`, `This brand cannot be deleted because it is currently referenced by other modules:`, `- Fixed Asset (1 asset name)` (bentuk singular), dan `Please remove these references before deleting the brand.`
5. Verifikasi hanya ada satu tombol `[OK]` (text, contrast)
6. Verifikasi tidak ada toast

### TC-GS-BRAND-100: Klik OK dialog blokir menutup dialog tanpa menghapus

7. Klik [OK]
8. Verifikasi dialog tertutup
9. Verifikasi Acme Corp tetap di tabel

### TC-GS-BRAND-97: Delete Brand in-use menampilkan dialog blokir dengan breakdown Vertex Labs

10. Cari baris Vertex Labs (lewat pagination atau Search), lalu klik `⋯` > Delete
11. Verifikasi dialog blokir `Cannot Delete Brand` (warning) tampil
12. Verifikasi Body memuat `• Vertex Labs`, `This brand cannot be deleted because it is currently referenced by other modules:`, `- Fixed Asset (2 asset names)`, `- Supply (3 item types)` dengan urutan tetap (modul dengan jumlah 0 tidak tampil), dan `Please remove these references before deleting the brand.`
13. Verifikasi hanya ada satu tombol `[OK]` (text, contrast)
14. Verifikasi tidak ada toast
15. Klik [OK]

### Ganti akun ke Principal

16. Logout dari akun Total Control Client A
17. Login sebagai Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`) pada instance Principal
18. Buka Global Settings > Master Reference > Brand

### TC-GS-BRAND-99: Delete Brand dipakai Device SKU pada instance Principal

19. Cari baris Signal One (lewat pagination atau Search), lalu klik `⋯` > Delete
20. Verifikasi dialog `Cannot Delete Brand` tampil dengan Body `• Signal One` dan `- Admin Console (3 device SKUs)`
21. Verifikasi tombol `[OK]` tampil
22. Klik [OK]

### TC-GS-BRAND-101: Referensi Device SKU tetap dihitung, referensi di Recycle Bin tidak

23. Cari baris Relic Co, lalu klik `⋯` > Delete
24. Verifikasi dialog blokir `Cannot Delete Brand` tampil dengan `- Admin Console (1 device SKU)`
25. Klik [OK]
26. Cari baris Ghost Co, lalu klik `⋯` > Delete
27. Verifikasi dialog `Delete Brand` (dialog konfirmasi biasa) tampil, bukan dialog blokir `Cannot Delete Brand`
28. Klik [Cancel]

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sourceTc: TC-100 (klik OK) disisipkan langsung setelah TC-96 karena memakai dialog yang sama (langkah "Klik `⋯` > Delete" TC-100 sumber digabung ke langkah 2), sehingga TC-97 (Vertex Labs) sesudahnya. Tidak ada aksi yang menghapus data di spec ini.
- Spec memakai dua akun (Client A dan Principal) dengan langkah ganti akun eksplisit (subjudul Ganti akun ke Principal), sesuai pengecualian bagian 3 "Tidak boleh" (a).
- Langkah penghubung: klik [OK] atau [Cancel] pada dialog Vertex Labs (langkah 15), Signal One (langkah 22), dan Ghost Co (langkah 28) ditulis sebagai aksi tanpa `Verifikasi` untuk menutup dialog; TC sumber tidak menyebut penutupan tersebut. Klik [OK] pada Relic Co (langkah 25) adalah Langkah Uji TC-101.
- Brand pre-setup tidak diberi suffix `{runId}` karena tidak dibuat atau diubah spec ini.
