---
id: TC-GS-HHR-E2E-009-role-matrix-negatif-akses-langsung-url
title: "Role Matrix Negatif: Akses Langsung URL Handheld Reader oleh Akun Tanpa Capability"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-35
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Langsung URL Handheld Reader oleh Akun Tanpa Capability

## Prerequisites

- Mode: FE+BE. Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Role yang diuji (Tabel Data Uji Pre-setup #7, Client A):

| Role | Nama user | Email | Env var password |
|---|---|---|---|
| Tanpa Capability | Hendra Gunawan | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Login Tanpa Capability dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Layar awal: halaman utama Global Settings dibuka di hook `beforeEach`.
- Data: Client A memiliki Seed Reader A (DD-01 s.d. DD-10, disiapkan fixture BE yang disediakan tim FE); spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada.

## Test Steps

### Akses URL langsung tanpa capability

1. Ketik URL halaman `Global Settings > Hardware > Handheld Reader` langsung di address bar, lalu tekan Enter
2. Verifikasi muncul toast error "You don't have permission to do this."
3. Verifikasi tidak ada redirect ke halaman unauthorized
4. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tersembunyi
5. Verifikasi data reader Client A tidak tampil

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 2). Spec Role Matrix negatif tersendiri per topik (akses langsung URL bukan soal "aksi ditolak"), sehingga terpisah dari spec visibilitas elemen per role (`TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role`).
- Langkah 3 memakai halaman yang tetap berada pada halaman setelah toast sebagai dasar "tidak ada redirect" (URL dan halaman tidak berpindah ke halaman unauthorized). Toast pada langkah 2 menjadi anchor positif bagi asersi absence data pada langkah 5.
- Temuan untuk QA:
  - TC-GS-HHR-35 butir b ("UI di-refresh sehingga elemen yang tidak berhak tersembunyi") tidak menyebut elemen mana yang dicek; spec memakai satu `Verifikasi` umum dan tidak menambah asersi elemen tertentu.
  - TC-GS-HHR-35 tidak menyebut isi halaman yang tampil setelah toast (halaman kosong atau halaman utama Global Settings); butir c hanya menyatakan data reader Client A tidak tampil.
  - TC-GS-HHR-35 menyatakan "tidak ada redirect" tanpa menyebut URL yang diharapkan pada address bar setelah toast.
